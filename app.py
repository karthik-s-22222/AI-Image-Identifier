import google.generativeai as genai
import numpy as np
import streamlit as st 
from tensorflow.keras.applications.mobilenet_v2 import ( MobileNetV2,preprocess_input,decode_predictions)
from PIL import Image

def load_model():
    model = MobileNetV2(weights ='imagenet')
    return model

def preprocess_image(image):
    img = image.convert("RGB")
    img = np.array(image)
    img = np.array(Image.fromarray(img).resize((224,224)))
    img = preprocess_input(img)
    img = np.expand_dims(img,axis=0)
    return img

def classify_image (model,image):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image) # type: ignore
        decoded_predictions = decode_predictions(predictions, top=1) [0]
        return decoded_predictions
    except Exception as e:
        st.error(f"Error classifying image: {str(e)}")
        return None
    
def main():
    st.set_page_config(page_title=" AI Image Identifier ", page_icon="✨", layout="centered")

    # --- ADDING COLOUR WITH CUSTOM CSS ---
    st.markdown("""
        <style>
        .stApp {
            background-color: #f0f2f6;
        }
        .main-title {
            color: #2E4053;
            text-align: center;
            font-family: 'Helvetica';
        }
        div.stButton > button:first-child {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-weight: bold;
        }
        .prediction-text {
            color: #1A5276;
            font-size: 20px;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-title"> 🔍 AI Image Identifier </h1>', unsafe_allow_html=True)
    st.write("Upload an image to identify it using Artificial Intelligence.")

    @st.cache_resource
    def load_cached_model():
        return load_model()
    
    model= load_cached_model()

    uploaded_file = st.file_uploader (" upload an image.", type=['jpeg','png'])
    
    if uploaded_file is not None:
        st.image(
            uploaded_file, caption='Uploaded Image', use_container_width=True
        )
        if st.button("Analyze Image Deeply"):
            with st.spinner("Analyzing Your Image..."):
                image = Image.open(uploaded_file)
                predictions= classify_image(model, image)
                 
                if predictions:
                    for _, label, score in predictions:
                            clean_label = label.replace('_', ' ')
                            st.write(f"**{clean_label}**")
                            st.progress(float(score))
                            st.caption(f"Match Probability: {score:.2%}")
            st.success("Image analysis complete!")

if __name__== "__main__":
    main()