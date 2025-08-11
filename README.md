# Agentstack
This project demonstrates how to build, containerize, and deploy an intelligent AI agent using Python and Docker.

## 📌 Description
A supervisor orchestrates a research agent and an inbox management agent to **read**, **summarize**, and **send** actionable emails.  
Built with **FastAPI**, **LangGraph**, and **OpenAI API**, integrated with real tools (send/read email) and structured output via **Pydantic**.

---

## 🛠️ Tech Stack
- **Backend**: FastAPI
- **Agent Orchestration**: LangGraph / LangChain
- **Language Models**: OpenAI API (configurable `OPENAI_BASE_URL`)
- **Persistence**: SQLModel / PostgreSQL
- **Infrastructure**: Docker, docker-compose
- **Data Validation**: Pydantic
- **Email I/O**: Custom tools (`send_mail`, `read_inbox`)

---

## ✨ Features
- **Multi-agent**:
  - `email_agent`: Manages inbox and sending emails.
  - `research_agent`: Prepares email drafts based on user queries.
  - **Supervisor**: Decides when and how to use each agent.
- **Real tools**:
  - `send_me_email(subject, content)`
  - `get_unread_emails(hours_ago)`
  - `research_email(query)`
- **Structured Output** with Pydantic (`EmailMessageSchema`)
- **Docker-ready**
- **Extensible**: possible RAG integration (FAISS/ChromaDB) for knowledge-base search.
- **Database integration** for caching responses and logging metrics.


## 📂 Estructura del proyecto
