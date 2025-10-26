import os
from fpdf import FPDF
from PyPDF2 import PdfReader
from datetime import datetime
import google.generativeai as genai

# For Streamlit secrets if deployed
try:
    import streamlit as st
    API_KEY = st.secrets["general"]["GOOGLE_API_KEY"]
except Exception:
    # Fallback for local testing using .env
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Set it in .env or Streamlit secrets.")

# Configure the generative AI model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

# Function to get AI response based on input and prompt
def SendRequest(input_text, pdf_content, prompt):
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

# Function to extract text from PDF 
def ExtractPDF(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text 

# Function to create an optimized PDF
def CreatePDF(text, input_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_margins(10, 10, 10)
    pdf.set_font("Courier", size=10)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'), align='L')
    timestamp = datetime.now().strftime("%d%m%Y-%H%M%S")
    file_name = f"{input_filename}_Optimized_{timestamp}.pdf"
    pdf.output(file_name, 'F')
    return file_name if os.path.exists(file_name) else None
