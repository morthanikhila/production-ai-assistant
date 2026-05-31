from haystack.utils import Secret

from haystack_integrations.document_stores.pinecone import PineconeDocumentStore

from app.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX
)


def get_document_store():

    document_store = PineconeDocumentStore(
        api_key=Secret.from_token(PINECONE_API_KEY),
        index=PINECONE_INDEX,
        namespace="default",
        dimension=384,
        metric="cosine"
    )

    return document_store