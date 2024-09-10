import os
from typing import Any, List, Optional

from loguru import logger
from swarms.models.tiktoken_wrapper import TikTokenizer
from swarms_memory.vector_dbs import ChromaDB
from pydantic import BaseModel

from omniparse.utils import chunk_text_dynamic, file_to_string


class OmniParseOutputLog(BaseModel):
    number_of_tokens: int
    context: str
    agent_output: Any


class OmniParseOutput(BaseModel):
    collection_name: str
    logs: List[OmniParseOutputLog]
    limit_tokens: int
    db_n_results: int
    document_name: Optional[str]
    document_names: Optional[List[str]]


class OmniParse:
    def __init__(
        self,
        model: Optional[Any] = None,
        collection_name: str = "omniparse",
        db_n_results: int = 10,
        document_name: Optional[str] = None,
        document_names: Optional[List[str]] = None,
        limit_tokens: int = 10000,
        log_level: str = "INFO",
    ):
        """
        Initialize OmniParse.

        Args:
            model (Optional[Any]): The model to use for parsing.
            collection_name (str): Name of the ChromaDB collection.
            db_n_results (int): Number of results to retrieve from the database.
            document_name (Optional[str]): Single document to parse.
            document_names (Optional[List[str]]): List of documents to parse.
            limit_tokens (int): Token limit for text chunking.
            log_level (str): Logging level (e.g., "INFO", "DEBUG").
        """
        self.model = model
        self.memory = ChromaDB(
            output_dir=collection_name,
            n_results=db_n_results,
            limit_tokens=limit_tokens,
        )
        self.document_name = document_name
        self.document_names = document_names
        self.limit_tokens = limit_tokens

        # Configure logging
        logger.remove()
        logger.add(
            f"{collection_name}.log",
            rotation="10 MB",
            retention="1 week",
            level=log_level,
        )
        logger.add(lambda msg: print(msg, end=""), level=log_level)

        logger.info(
            f"Initialized OmniParse with collection_name: {collection_name}"
        )

        # Add documents to memory
        self._add_docs_to_memory()

        # Set up output log
        self.output_log = OmniParseOutput(
            collection_name=collection_name,
            logs=[],
            limit_tokens=limit_tokens,
            db_n_results=db_n_results,
            document_name=document_name,
            document_names=document_names,
        )

    def _add_docs_to_memory(self):
        """Add documents to the ChromaDB memory."""
        try:
            if self.document_name:
                self._add_single_document(self.document_name)
            elif self.document_names:
                for document_name in self.document_names:
                    self._add_single_document(document_name)
            else:
                raise ValueError("No document name or names provided")
        except Exception as e:
            logger.error(
                f"Error adding documents to memory: {str(e)}"
            )
            raise

    def _add_single_document(self, document_path: str):
        """
        Add a single document to the ChromaDB memory.

        Args:
            document_path (str): Path to the document.
        """
        if not os.path.exists(document_path):
            logger.error(f"Document not found: {document_path}")
            return

        try:
            doc_data = file_to_string(document_path)
            self.memory.add(doc_data)
            logger.info(f"Added document {document_path} to memory")
        except Exception as e:
            logger.error(
                f"Error processing {document_path}: {str(e)}"
            )

    def _run_agent(self, query: str) -> str:
        """
        Run a query against the parsed documents.

        Args:
            query (str): The query string.

        Returns:
            List[str]: Chunked context relevant to the query.
        """
        return self.model.run(query)

    def run(self, query: str) -> List[str]:
        """
        Run a query against the parsed documents.

        Args:
            query (str): The query string.

        Returns:
            List[str]: Chunked context relevant to the query.
        """
        logger.info(f"Running query: {query}")
        try:
            context = self.memory.query(query)
            token_count = TikTokenizer().count_tokens(context)
            logger.info(
                f"Retrieved context with {token_count} tokens"
            )

            chunked_context = chunk_text_dynamic(
                context, limit_tokens=self.limit_tokens
            )
            logger.info(
                f"Chunked context into {len(chunked_context)} parts"
            )

            # For chunked context, run the agent
            for chunk in chunked_context:
                agent_output = self._run_agent(chunk)
                logger.info(f"Agent output: {agent_output}")

                self.output_log.logs.append(
                    OmniParseOutputLog(
                        number_of_tokens=self.limit_tokens,
                        context=chunk,
                        agent_output=agent_output,
                    )
                )

            return self.output_log.model_dump_json(indent=4)
        except Exception as e:
            logger.error(f"Error running query: {str(e)}")
            raise


# if __name__ == "__main__":
#     logger.add("omniparse.log", rotation="500 MB")  # Add file logging

#     try:
#         parser = OmniParse(
#             document_name="doc.pdf",
#             db_n_results=3,
#             limit_tokens=1000,
#             collection_name="omniparse_db",
#         )
#         context = parser.run("What is the total amount due?")
#         print(f"Context: {context[0]}")
#     except Exception:
#         logger.exception("An error occurred in the main execution")
