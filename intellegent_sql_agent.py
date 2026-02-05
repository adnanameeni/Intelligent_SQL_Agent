import os
os.environ["GROQ_API_KEY"] = "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"

from typing import TypedDict
from langgraph.graph import StateGraph, END
from groq import Groq
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///college.db")
client = Groq()

class AgentState(TypedDict):
    question: str
    sql_query: str
    result: str
class AgentState(TypedDict):
    question: str
    sql_query: str
    result: str

def generate_sql(state: AgentState):
    question = state["question"]

    prompt = f"""
You are an SQL expert.

Database table:
students(id, name, department, gpa)

Convert this question into SQL.
Return only SQL query.

Question: {question}
"""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    sql_query = completion.choices[0].message.content.strip()

    return {"sql_query": sql_query}

import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    gpa REAL
)
""")

cursor.executemany("""
INSERT INTO students (name, department, gpa)
VALUES (?, ?, ?)
""", [
    ("Ali", "CS", 3.5),
    ("Ahmed", "ME", 3.8),
    ("Sara", "CS", 3.9),
    ("Zara", "CSE", 3.6)
])

conn.commit()
conn.close()

print("Database Ready")

def run_sql(state: AgentState):
    query = state["sql_query"]

    try:
        with engine.connect() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

        return {"result": str(rows)}

    except Exception as e:
        return {"result": str(e)}

graph = StateGraph(AgentState)

graph.add_node("generate_sql", generate_sql)
graph.add_node("run_sql", run_sql)

graph.set_entry_point("generate_sql")
graph.add_edge("generate_sql", "run_sql")
graph.add_edge("run_sql", END)

app = graph.compile()

response = app.invoke({
    "question": "Who has the highest GPA?"
})

print("SQL Query:", response["sql_query"])
print("Result:", response["result"])

