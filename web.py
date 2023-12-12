import streamlit as st
import functions

todos = functions.get_todos()

st.title("My todo app")
st.subheader("This my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)


st.text_input("Todo", placeholder="Add a new todo...")
