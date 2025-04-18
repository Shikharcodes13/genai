from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

from langchain_qdrant import QdrantVectorStore



pdf_path = Path(__file__).parent/ "nodejs.pdf"
loader = PyPDFLoader(file_path=pdf_path)

docs=loader.load()

text_spliiter= RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs=text_spliiter.split_documents(documents=docs)


embedder= OpenAIEmbeddings(
    model="text-embedding-ada-002",
    
    
)

# vector_store= QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333",
#     collection_name="learning_langchain",
#     embedding=embedder,

# )

# vector_store.add_documents(documents=split_docs)

# print("Injection Done")



retriever=QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder,
)


search_result= retriever.similarity_search(
    query="what is FS Module?"
)

print("Relevant Chunks", search_result)