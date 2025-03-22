import requests
import streamlit as st

# Function to interact with the DeepSeek API (Essay Endpoint)
def get_deepseek_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={"input": {"topic": input_text}}
        )

        # Check if request was successful
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("output", "No content received")
            except ValueError:
                return f"Error: Received non-JSON response: {response.text}"
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Function to interact with the Groq API (Poem Endpoint)
def get_groq_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={"input": {"topic": input_text}}
        )

        # Check if request was successful
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("output", "No output received")
            except ValueError:
                return f"Error: Received non-JSON response: {response.text}"
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Streamlit Framework for User Interface
st.title("Langchain Demo With DeepSeek and LLaMA-3")

# User Inputs
input_text = st.text_input("Enter a topic for the essay")
input_text1 = st.text_input("Enter a topic for the poem")

# Generating and Displaying the Results
if input_text:
    st.subheader("Generated Essay:")
    st.write(get_deepseek_response(input_text))

if input_text1:
    st.subheader("Generated Poem:")
    st.write(get_groq_response(input_text1))
