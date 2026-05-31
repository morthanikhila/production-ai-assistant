from haystack import Pipeline
from haystack.components.converters import PyPDFToDocument
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack.components.writers import DocumentWriter

from app.services.pinecone_service import get_document_store


document_store = get_document_store()


def build_ingestion_pipeline():

    pipeline = Pipeline()

    pipeline.add_component(
        "converter",
        PyPDFToDocument()
    )

    pipeline.add_component(
        "splitter",
        DocumentSplitter(
            split_by="word",
            split_length=200,
            split_overlap=50
        )
    )

    pipeline.add_component(
        "embedder",
        SentenceTransformersDocumentEmbedder(
            model="sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    pipeline.add_component(
        "writer",
        DocumentWriter(document_store=document_store)
    )

    pipeline.connect("converter", "splitter")
    pipeline.connect("splitter", "embedder")
    pipeline.connect("embedder", "writer")

    return pipeline