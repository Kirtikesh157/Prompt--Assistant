import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Prompt Engineering Assistant",
    page_icon="🤖",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: white;
}

/* Main content */
.main {
    background-color: #000000;
}

/* Text Area */
.stTextArea textarea {
    background-color: #111111;
    color: white;
    border: 1px solid #444444;
}

/* Buttons */
.stButton > button {
    background-color: #222222;
    color: white;
    border: 1px solid white;
    border-radius: 8px;
    width: 100%;
    height: 45px;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #444444;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file.")
    st.stop()

# -------------------------------
# Gemini Client
# -------------------------------
client = genai.Client(api_key=api_key)

# -------------------------------
# Load System Prompt
# -------------------------------
with open("PEA.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

# -------------------------------
# UI

# -------------------------------
st.image("image.png", width=800)

st.title("🤖 Prompt Engineering Assistant")

st.write("Transform simple prompts into detailed AI-ready prompts.")

user_prompt = st.text_area(
    "Enter your Prompt:",
    height=200,
    placeholder="Example: I want to build an AI app for students."
)

# -------------------------------
# Generate Button
# -------------------------------
if st.button("Generate Prompt"):

    if not user_prompt.strip():
        st.warning("⚠ Please enter a prompt.")
    else:

        final_prompt = f"""
{system_prompt}

User Prompt:
{user_prompt}
"""

        try:
            with st.spinner("Generating..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=final_prompt
                )

            st.subheader("✨ Improved Prompt")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")