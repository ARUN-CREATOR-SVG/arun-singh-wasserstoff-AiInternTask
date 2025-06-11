import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API keys and constants
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# You can define model names or other config here too
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

# Directories
DATA_PATH = "./backend/data/"
DB_DIR = "./backend/FAISS_db"
