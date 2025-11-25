import google.generativeai as genai
import streamlit as st
st.title("AI")

genai.configure(api_key='TBD')
model = genai.GenerativeModel('gemini-2.5-pro')

uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])



prompt = (
    "You are a helpful assistant that analyzes fruits and vegetables for health, ripeness, "
    "and pesticide presence based on visual clues.\n\n"
    "Analyze a food item using these visual indicators:\n\n"
    "Pesticide Indicators:\n- Too perfect in appearance\n- Perfectly even color\n- Very bright, shiny, or glossy\n"
    "- Very large\n- No imperfections or marks\n- Lasts unusually long\n\n"
    "Low-Pesticide / Natural Indicators:\n- Smaller size\n- Dull or matte appearance\n- Tiny marks or blemishes\n"
    "- Uneven color\n\n"
    "Tasks:\n1. Determine whether the food likely has pesticides, whether it is waxed, and whether it is ripe or rotten.\n"
    "2. Write a 30-word paragraph explaining how healthy or unhealthy the food appears based on visual clues.\n"
    "3. provide percentage estimates for Rotten, Ripe, Pesticides, and Wax, be exact.\n"
)

contents = [{"text": prompt}]

if uploaded_image:
    st.image(uploaded_image)
    image_bytes = uploaded_image.read()
    with st.spinner("Analyzing image..."):
        response = model.generate_content(
            [prompt, {"mime_type": uploaded_image.type, "data": image_bytes}]
        )

    st.write(f"AI: {response.text}")


