import streamlit as st
import random

st.title("🎭 Deepfake Detection System")

file = st.file_uploader("Upload Image or Video")

if file:
    st.write("Processing...")

    # Fake prediction
    fake_score = random.uniform(40, 80)
    real_score = 100 - fake_score

    st.subheader("Detection Results")
    st.write(f"Deepfake Confidence: {fake_score:.2f}%")
    st.write(f"Real Confidence: {real_score:.2f}%")

    st.progress(int(fake_score))
