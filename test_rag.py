from app.pipelines.rag_pipeline import ask_question


question = input("Ask a question: ")

answer = ask_question(question)

print("\n")
print("=" * 50)
print("ANSWER")
print("=" * 50)
print(answer)