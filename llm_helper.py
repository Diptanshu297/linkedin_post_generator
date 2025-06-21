import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3-70b-8192"
)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are")
    print(response.content)






