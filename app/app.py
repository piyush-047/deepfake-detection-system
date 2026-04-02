import streamlit as st
import random

st.set_page_config(page_title="Deepfake Detector", layout="centered")

st.title("🎭 Advanced Deepfake Detection System")
st.write("Upload an image or video to detect deepfake content.")

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "mp4"])

if uploaded_file:
    st.success("File uploaded successfully!")

    # Fake detection simulation
    fake_score = round(random.uniform(45, 65), 2)
    real_score = 100 - fake_score

    st.subheader("📊 Detection Results")
    st.write(f"Deepfake Confidence: {fake_score}%")
    st.write(f"Authentic Confidence: {real_score}%")

    st.progress(fake_score / 100)

    st.subheader("📌 Basis for Detection")
    st.write("""
    - Temporal inconsistencies detected in facial movements
    - Frame-level irregularities observed
    - Possible mismatch in lighting and expression patterns
    """)

    st.subheader("📜 Scan History")
    st.write("Recent scan logged successfully")

    st.warning("⚠️ This is a simulated model for demonstration purposes.")
