# testar_env.py — confere se a key da Groq está no .env
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("Key Groq carregada! Começa com:", api_key[:7], "...")
else:
    print("Key não encontrada — crie o arquivo .env com GROQ_API_KEY=...")
