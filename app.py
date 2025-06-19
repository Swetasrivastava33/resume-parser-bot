import os


import streamlit as st
import fitz  # PyMuPDF
import docx2txt
from parser import extract_name, extract_skills, extract_education

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def read_docx(file):
    return docx2txt.process(file)

st.set_page_config(page_title="Resume Parser Bot", layout="centered")
st.title("📄 Resume Parser Bot")

uploaded_file = st.file_uploader("Upload a Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = read_pdf(uploaded_file)
    else:
        text = read_docx(uploaded_file)

    st.subheader("🔍 Parsed Information")
    name = extract_name(text)
    skills = extract_skills(text)
    education = extract_education(text)

    st.write(f"**Name:** {name or 'Not found'}")
    st.write(f"**Skills:** {', '.join(skills) if skills else 'Not found'}")
    st.write(f"**Education:** {', '.join(education) if education else 'Not found'}")

    with st.expander("📄 Raw Text from Resume"):
        st.text(text)
