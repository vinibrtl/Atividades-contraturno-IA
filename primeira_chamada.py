# primeira_chamada.py — primeira conversa com a Groq (sem função ainda)
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

body = {
    "model": "openai/gpt-oss-20b",
    "messages": [
        {"role": "user", "content": "Explique o que é Python em 1 frase"}
    ],
}

resposta = requests.post(url, headers=headers, json=body, timeout=30)
dados = resposta.json()

print("Status:", resposta.status_code)
print(dados)

if resposta.status_code == 429:
    print("\nLimite do free tier da Groq (muitas requisições). Espere 1 minuto e tente de novo.")
elif resposta.status_code == 401:
    print("\nAPI key inválida. Confira o arquivo .env (GROQ_API_KEY).")
elif resposta.status_code != 200:
    print(f"\nErro da API (status {resposta.status_code}).")
else:
    texto = dados["choices"][0]["message"]["content"]
    print("\n--- Resposta ---")
    print(texto)
