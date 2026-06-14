from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import PGVector
from app.config import settings

CONNECTION_STRING = settings.DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://")
# Changed collection name to force a new table for 384-dimension vectors
COLLECTION_NAME = "dishant_portfolio_hf_vectors"

def get_vector_store():
    # Running embeddings locally for free instead of paying OpenAI
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return PGVector(
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING,
    )

async def stream_ai_response(query: str, chat_history: list):
    store = get_vector_store()
    docs = store.similarity_search(query, k=3)
    context = "\n---\n".join([doc.page_content for doc in docs])

    system_prompt = f"""
    You are the personal AI twin and portfolio assistant for Dishant Sharma.
    Your sole purpose is to answer questions regarding his software engineering background, MERN stack expertise, React Native applications, and technical metrics.

    CRITICAL RULES:
    1. Base your answers strictly on the context provided below.
    2. If the prompt asks about general knowledge, programming challenges outside his history, or unrelated topics, execute this hard safety response:
       "I am Dishant's personal AI portfolio assistant. My knowledge is limited to information about Dishant Sharma, his experience, projects, skills, and public profiles. I cannot answer general-purpose questions."
    3. Adopt an articulate, high-level engineering consultant persona.

    Retrieved Context:
    {context}
    """

    messages = [{"role": "system", "content": system_prompt}]
    for msg in chat_history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": query})

    # Hooking LangChain's OpenAI wrapper into OpenRouter's Base URL
    llm = ChatOpenAI(
        model="openrouter/free",
        api_key=settings.OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.1,
        streaming=True
    )
    
    async for chunk in llm.astream(messages):
        yield f"data: {chunk.content}\n\n"