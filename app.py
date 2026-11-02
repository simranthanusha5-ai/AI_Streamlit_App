import streamlit as st
st.title("AI-enabled Web Application")
st.write("welcome to ai enable web application using streamlit community cloud")
name=st.text_input("enter your name")
if st.button("Submit"):
    st.write(f"hello,{name}! your  application is running successfully")
