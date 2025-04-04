import streamlit as st
import requests

st.title("Code Plagiarism Detector")

code_input = st.text_area("Enter your code here:")

if st.button("Submit"):
    if code_input:
        response = requests.post("http://localhost:8001/check", json={"code": code_input})
        
        if response.status_code == 200:
            st.write("API Response:")
            st.write(response.json())
        else:
            st.write("Error:", response.status_code)
    else:
        st.write("Please enter some code.")
