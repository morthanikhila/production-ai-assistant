from app.pipelines.ingestion_pipeline import build_ingestion_pipeline

pipeline = build_ingestion_pipeline()

pipeline.run({
    "converter": {
        "sources": ["data/machinelearning.pdf"]
    }
})

print("Documents indexed successfully!")