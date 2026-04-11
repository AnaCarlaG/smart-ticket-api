# 🎫 Smart Ticket API

API REST desenvolvida em Python com FastAPI que utiliza IA (LLaMA 3 via Groq) para analisar chamados de suporte de TI em texto livre e retornar automaticamente categoria, prioridade, resumo e sugestão de resposta — reduzindo o tempo de triagem e melhorando a eficiência do time de suporte.

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tech Stack](#tech-stack)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Endpoints](#endpoints)
- [Exemplo](#exemplo)
- [Autora](#autora)

---

## Sobre o Projeto

Times de suporte de TI frequentemente recebem chamados com descrições vagas e mal categorizadas, fazendo com que tickets críticos fiquem parados na fila errada e o SLA seja comprometido.

A **Smart Ticket API** resolve esse problema recebendo a descrição do problema em texto livre e retornando uma resposta estruturada com categoria, prioridade, resumo e sugestão de resposta inicial — tudo gerado automaticamente por um modelo de linguagem. O resultado é uma triagem mais rápida, consistente e sem depender do julgamento manual de cada atendente.

---

## Tech Stack

- **Python 3.11+**
- **FastAPI** — framework web para construção da API REST
- **Uvicorn** — servidor ASGI
- **httpx** — cliente HTTP assíncrono para chamadas externas
- **Pydantic** — validação e serialização de dados
- **Groq API** — LLaMA 3 (plano gratuito)
- **Swagger UI** — documentação interativa gerada automaticamente pelo FastAPI

---

## Pré-requisitos

- Python 3.11 ou superior
- Conta gratuita no [Groq Console](https://console.groq.com) para obter a API Key
- Git

---

## Instalação

```bash
# Clone o repositório
git clone https://github.com/AnaCarlaG/smart-ticket-api.git
cd smart-ticket-api

# Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

---

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions
GROQ_API_KEY=sua_chave_aqui
GROQ_MODEL=llama-3.1-8b-instant
```

> ⚠️ Nunca compartilhe sua API Key. O arquivo `.env` já está no `.gitignore`.

---

## Como Usar

Suba o servidor:

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa no navegador:

```
http://localhost:8000/docs
```

---

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Verifica se a API está no ar |
| POST | `/api/tickets/analyze` | Analisa e classifica um chamado |

---

## Exemplo

**Requisição:**

```json
POST /api/tickets/analyze

{
  "description": "Meu computador não liga desde essa manhã e tenho uma reunião em 1 hora"
}
```

**Resposta:**

```json
{
  "id": 1,
  "title": "Computador não inicializa",
  "category": "Hardware",
  "priority": "ALTA",
  "summary": "Computador sem inicializar antes de reunião urgente",
  "suggested_response": "Recebemos seu chamado e ele foi marcado como alta prioridade. Um técnico entrará em contato em até 15 minutos."
}
```

---

## Autora

**Ana Carla G.**  
[GitHub](https://github.com/AnaCarlaG)
