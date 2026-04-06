import streamlit as st
from snowflake.snowpark.context import get_active_session

session = get_active_session()

st.title("✏️ Generate Haikus")
st.write("Enter the topic of your choice to get back an original haiku!")

topic = st.text_input("Haiku Topic")

if topic:
    try:
        result = session.sql("SELECT SF_LLM.PUBLIC.GEN_HAIKU(?)", params=[topic]).collect()
        st.write(result[0][0])
    except Exception as e:
        st.error(f"Error: {e}")