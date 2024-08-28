import os
import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key=("AIzaSyClqSzrXiCLgKeRJKGT2vYHAMi6lHbfVVw"))

# Set up the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the GenerativeModel
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Create the Streamlit app
st.title("Gemini AI Speech Generator")

# Input from user
user_input = st.text_area("Enter text to generate speech:", placeholder="Type here...")

# Speech duration input (in seconds)
duration = st.slider("Set the duration for the speech (in seconds):", min_value=5, max_value=300, value=60)

# Button to generate speech
if st.button("Generate Speech"):
    if user_input:
        # Start chat session
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [f"Generate a speech of about {duration} seconds based on the following text: {user_input}"],
                },
            ]
        )
        
        # Send message to model and get response
        response = chat_session.send_message(f"Generate a speech of about {duration} seconds based on the following text: {user_input}")
        
        # Display the generated text
        st.write("### Generated Speech:")
        st.write(response.text)
    else:
        st.warning("Please enter some text before generating speech.")
