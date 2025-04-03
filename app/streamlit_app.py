import streamlit as st
import requests

# Streamlit app title
st.title("Code Plagiarism Detector")

# Text area for code input
code_input = st.text_area("Enter your code here:")

# Submit button
if st.button("Submit"):
    if code_input:
        # Send request to the API
        response = requests.post("http://localhost:8001/check", json={"code": code_input})
        
        if response.status_code == 200:
            st.write("API Response:")
            st.write(response.json())
        else:
            st.write("Error:", response.status_code)
    else:
        st.write("Please enter some code.")
