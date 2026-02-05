import streamlit as st
from setup_database import create_database
from intellegent_sql_agent import app as agent_app  # Import your LangGraph agent

create_database()

st.title("Intelligent SQL Agent")

st.markdown("""
Ask questions about the students database in **plain English**.  
The SQL agent will generate SQL queries and return results.
""")

# User input
question = st.text_input("Enter your question:")

if st.button("Run"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
        
            response = agent_app.invoke({"question": question})

            # Display the generated SQL
            st.subheader("Generated SQL")
            st.code(response["sql_query"])

            # Display the result
            st.subheader("Result")
            st.write(response["result"])
        except Exception as e:
            st.error(f"Error: {e}")
