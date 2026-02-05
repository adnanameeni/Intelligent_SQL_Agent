An **Intelligent SQL Agent** built with Python, SQLite, LangGraph, and Streamlit that allows users to ask questions about a database in **plain English**, and automatically generates SQL queries to fetch the results. This project combines NLP and database automation for simplified data access.

---

## Project Overview

Traditional SQL querying can be difficult for non-technical users or even developers for complex queries. This project provides a **modular, node-based intelligent agent** that:

- Understands natural language questions
- Dynamically explores database schema
- Generates error-free SQL queries
- Returns results in a user-friendly UI

---

## Requirements

- Python 3.10+
- Install dependencies using pip:

```bash
pip install langchain langgraph groq sqlalchemy streamlit pyngrok python-dotenv
