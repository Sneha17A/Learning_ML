import streamlit as st
from snowflake.snowpark.context import get_active_session

session = get_active_session()

st.title("✏️ Explain this topic")
st.write("Enter the topic of your choice to get back an information!")

topic = st.text_input("Topic")

# Build the SQL statement to generate the topic 
#function_call = "select gen_haiku (" + topic_entered +  ")"
function_call = "select ask_mon_ami ('" + topic + "')"

#st.write ("This is the SQL that will be run: ", function_call)
# run the SQL code 
session = get_active_session( )
new_topic = session.sql(function_call)

# display the topic 
st.write(new_topic)
