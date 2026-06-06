import google.generativeai as genai

from app.config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(context, question):

    prompt = f"""
    You are a helpful AI assistant.

    Context:
    {context}

    Question:
    {question}

    Answer only from the provided context.
    If the answer is not present, say:
    "I could not find that information in the document."
    """

    response = model.generate_content(prompt)

    return response.text