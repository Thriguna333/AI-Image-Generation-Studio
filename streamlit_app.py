import streamlit as st

st.title("🎨 AI Image Generation Studio")

st.subheader("Text-to-Image")

prompt = st.text_input("Enter Prompt")

if st.button("Generate"):
    st.success(f"Generating image for: {prompt}")

st.markdown("---")
st.write("Developed by Manikonda Saithriguna")