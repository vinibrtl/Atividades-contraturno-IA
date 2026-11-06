# devido ao free tier do groq
LIMITE_CARACTERES = 6000

# def -> function do js
def carregar_contexto(caminho: str = "contexto.txt") -> str:
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            texto = arquivo.read().strip()
    except FileNotFoundError:
        print(f"Aviso: arquivo '{caminho}' não encontrado. Seguindo sem contexto.")
        return ""
    
    if len(texto) > LIMITE_CARACTERES:
        print(f"Aviso: o arquivo tem mais caracteres que o permitido. Utilizando apenas os primeiros 6000")
            texto = texto[:LIMITE_CARACTERES]

    return texto

# variavel privada __aaa__
if __name__ == "__main__":
    conteudo = carregar_contexto()
    print(conteudo)
    print("\nTotal de caracteres:", len(conteudo))