from app.pipelines.retrieval_pipeline import (
    build_retrieval_pipeline
)

pipeline = build_retrieval_pipeline()

results = pipeline.run(
    {
        "text_embedder": {
            "text": "What is machine learning?"
        }
    }
)

documents = results["retriever"]["documents"]

for i, doc in enumerate(documents, start=1):
    print("\n")
    print("=" * 50)
    print(f"Document {i}")
    print("=" * 50)
    print(doc.content)