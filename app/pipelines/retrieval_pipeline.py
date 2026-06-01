from haystack import Pipeline

from haystack.components.embedders import (
    SentenceTransformersTextEmbedder
)

from haystack_integrations.components.retrievers.pinecone import (
    PineconeEmbeddingRetriever
)

from app.services.pinecone_service import get_document_store


document_store = get_document_store()


def build_retrieval_pipeline():

    pipeline = Pipeline()

    pipeline.add_component(
        "text_embedder",
        SentenceTransformersTextEmbedder(
            model="sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    pipeline.add_component(
        "retriever",
        PineconeEmbeddingRetriever(
            document_store=document_store,
            top_k=3
        )
    )

    pipeline.connect(
        "text_embedder.embedding",
        "retriever.query_embedding"
    )

    return pipeline