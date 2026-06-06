from app.pipelines.retrieval_pipeline import build_retrieval_pipeline
from app.services.llm_service import generate_answer


def ask_question(question):

    pipeline = build_retrieval_pipeline()

    result = pipeline.run({
        "text_embedder": {
            "text": question
        }
    })

    documents = result["retriever"]["documents"]

    context = "\n\n".join(
        [doc.content for doc in documents]
    )

    answer = generate_answer(
        context=context,
        question=question
    )

    return answer