# Omni-Parse

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)

**OmniParse** is an enterprise-grade solution designed to transform unstructured documents into actionable, structured data with precision and reliability. Whether dealing with invoices, contracts, reports, or any other type of unstructured data, OmniParse is your go-to solution for seamless extraction, processing, and integration into your workflows.


## Features

- **Enterprise-Grade Precision**: OmniParse is built to handle large-scale document processing needs, ensuring high accuracy in extracting structured data from complex and varied document formats.
- **Scalable Architecture**: Optimized for deployment in production environments with the capability to handle high volumes of documents and complex workflows.
- **Customizable Extraction Pipelines**: Easily define and modify extraction rules to fit the unique structure of your documents.
- **Seamless Integration**: API-ready, OmniParse integrates effortlessly with your existing enterprise systems, ensuring smooth data flow into databases, ERP systems, or custom solutions.
- **High Performance**: Engineered for speed, OmniParse provides fast data extraction while maintaining a low resource footprint.
- **Advanced Document Types Support**: Support for PDFs, scanned images, and more, with OCR and natural language processing (NLP) capabilities to enhance data extraction.

## Use Cases

- **Finance**: Extract data from invoices, receipts, and financial reports for automated bookkeeping and reporting.
- **Legal**: Automate the extraction of key information from contracts, legal agreements, and court documents.
- **Healthcare**: Convert unstructured medical records into structured formats for easier integration with healthcare systems.
- **Logistics**: Parse shipment documents, bills of lading, and other transport-related paperwork for supply chain automation.
  
## Installation

To install **OmniParse**, use the following command:

```bash
pip install omniparse
```

Alternatively, you can clone this repository and install the dependencies manually:

```bash
git clone https://github.com/The-Swarm-Corporation/OmniParse.git
cd OmniParse
pip install -r requirements.txt
```

## Quickstart

Here’s a simple example to get started with **OmniParse**:

```python
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

```

## Documentation

For detailed documentation on how to customize your pipelines, configure extraction rules, and integrate **OmniParse** into your enterprise systems, visit the [documentation](https://docs.omniparse.io).

## Roadmap

- **Cloud Integration**: Future support for direct cloud integrations with AWS, Azure, and Google Cloud.
- **Advanced NLP Models**: Incorporating cutting-edge natural language processing for even more accurate data extraction.
- **Multi-Language Support**: Expanding capabilities to handle documents in multiple languages.

## Contributing

We welcome contributions from the open-source community! Please read our [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

OmniParse is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.



# License
MIT
