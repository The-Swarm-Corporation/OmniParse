from omniparse.main import OmniParse
from omniparse.prebuilt_agent import model

parser = OmniParse(
    model=model,
    document_name="doc.pdf",
    db_n_results=3,
    limit_tokens=1000,
    collection_name="omniparse_db",
)

context = parser.run("What is the total amount due?")
print(context)
