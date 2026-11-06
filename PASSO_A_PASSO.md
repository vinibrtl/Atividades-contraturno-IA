# Passo a passo — o que instalar e o que fazer (`aula-groq`)

Guia do zero até o chatbot funcionar.  
Provedor: **Groq** (grátis, sem cartão) · modelo: `openai/gpt-oss-20b`

> **Windows:** use `python` ou `py`  
> **Mac:** use `py`

---

## 1. O que você precisa ter instalado

| Item | Para quê | Onde baixar |
|---|---|---|
| **Python 3.11+** | Rodar os `.py` | [python.org/downloads](https://www.python.org/downloads/) |
| **VS Code** | Editor + terminal | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Extensão Python** (no VS Code) | Destacar código / Run | Aba Extensões → buscar “Python” (Microsoft) |
| Conta **Groq** + API key | Falar com a IA | [console.groq.com](https://console.groq.com) |

### Python no Windows (importante)

Na instalação, marque **"Add python.exe to PATH"**.  
Se `python` abrir a Microsoft Store sozinho:  
Configurações → Aplicativos → Aliases de execução → desligar os instaladores do Python.

### Conferir

```bat
python --version
```

```bash
py --version
```

Tem que aparecer algo como `Python 3.11` ou superior.

---

## 2. Criar a key da Groq (grátis)

1. Entre em [console.groq.com](https://console.groq.com) (login com Google/e-mail)  
2. Menu **API Keys** → **Create API Key**  
3. Dê um nome (ex.: `aula`) e copie a key  
4. Guarde: ela **só aparece uma vez**

Cada pessoa usa a **própria** key (não compartilhe a do colega/instrutor).

---

## 3. Abrir o projeto no VS Code

1. Baixe/copie a pasta `aula-groq` para o computador  
2. Abra o VS Code → **File → Open Folder…** → escolha `aula-groq`  
3. Abra o terminal: **Terminal → New Terminal**  
4. Confirme que o terminal está **dentro** da pasta `aula-groq`

```bat
cd aula-groq
```

(Se já abriu a pasta no VS Code, o `cd` pode não ser necessário.)

---

## 4. Instalar as bibliotecas Python

No terminal:

```bat
python -m pip install requests python-dotenv
```

```bash
py -m pip install requests python-dotenv
```

| Biblioteca | Para quê |
|---|---|
| `requests` | Fazer a chamada HTTP para a API da Groq |
| `python-dotenv` | Ler a key do arquivo `.env` |

Se der erro de `pip`, tente `py -m pip install requests python-dotenv`.

---

## 5. Criar o arquivo `.env` (a key secreta)

1. No VS Code, na pasta `aula-groq`, clique em **New File**  
2. Nome exatamente: `.env` (com o ponto na frente)  
3. Conteúdo (uma linha):

```
GROQ_API_KEY=cole_sua_key_aqui
```

Regras:
- Sem aspas  
- Sem espaço antes/depois do `=`  
- Não salve como `.env.txt`  
- Não compartilhe print com a key inteira  

Há um modelo em `.env.example` (sem a key real).

---

## 6. Testar na ordem

Rode **um por um** e só avance se o anterior passou.

```bat
python testar_ambiente.py
python testar_import.py
python testar_env.py
python primeira_chamada.py
python llm.py
python chat_basico.py
```

```bash
py testar_ambiente.py
py testar_import.py
py testar_env.py
py primeira_chamada.py
py llm.py
py chat_basico.py
```

| Passo | Esperado |
|---|---|
| `testar_ambiente.py` | `Ambiente local funcionando! (Groq)` |
| `testar_import.py` | Números (`4.0`, pi…) |
| `testar_env.py` | `Key Groq carregada! Começa com: ...` |
| `primeira_chamada.py` | `Status: 200` + frase sobre Python |
| `llm.py` | Frase explicando o que é API |
| `chat_basico.py` | Digite uma pergunta → resposta → `sair` |

### No chat (`chat_basico.py`)

```
você> ajuda
você> O que é uma lista em Python, em 1 frase?
você> sair
```

### Extra (memória)

```bat
python chat_memoria.py
```

```
você> Meu nome é Ana
você> Qual é o meu nome?
você> limpar
você> Qual é o meu nome?
```

---

## 7. Checklist rápido

- [ ] Python instalado (`python --version` / `py --version`)  
- [ ] VS Code + extensão Python  
- [ ] Conta Groq + key criada  
- [ ] Pasta `aula-groq` aberta no VS Code  
- [ ] `pip install requests python-dotenv` ok  
- [ ] Arquivo `.env` com `GROQ_API_KEY=...`  
- [ ] `primeira_chamada.py` com Status `200`  
- [ ] `chat_basico.py` conversando  

---

## Se algo der errado

| Problema | Solução |
|---|---|
| `'python' não é reconhecido` | Use `py` · reinstale Python com PATH · reinicie o VS Code |
| `ModuleNotFoundError: requests` | Rode de novo o `pip install` do passo 4 |
| Key não encontrada | `.env` na pasta `aula-groq` · nome `GROQ_API_KEY` · sem `.txt` |
| Status `401` | Key errada ou incompleta · crie outra em console.groq.com |
| Status `404` / model not found | Modelo desatualizado — avise o instrutor (hoje usamos `openai/gpt-oss-20b`) |
| Status `429` | Muitas requisições no free tier · espere 1 minuto |
| Sem internet / bloqueio | Outra rede ou hotspot |

---

## Documentos desta pasta

| Arquivo | Conteúdo |
|---|---|
| **Este** (`PASSO_A_PASSO.md`) | Instalar + configurar + primeiros testes |
| [`ROTEIRO.md`](./ROTEIRO.md) | Sequência de testes em sala (instrutor/turma) |
| [`CODIGOS.md`](./CODIGOS.md) | O que cada `.py` faz |
