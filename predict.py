import streamlit as st
from PIL import Image, ImageOps
import numpy as np
from utils import load_model, predict_image

def is_chest_xray(image: Image.Image) -> bool:
    """
    A basic check to see if the image resembles a chest X-ray.
    This checks:
    - whether image is mostly grayscale
    - aspect ratio (X-rays are usually taller than wide)
    - low color variance
    """
    gray_image = ImageOps.grayscale(image)
    np_img = np.array(gray_image)

    avg_pixel = np.mean(np_img)
    std_pixel = np.std(np_img)
    height, width = np_img.shape

    grayscale_similarity = std_pixel < 60
    vertical_orientation = height > width
    brightness_ok = 50 < avg_pixel < 200

    return grayscale_similarity and vertical_orientation and brightness_ok

def predict_page():
    st.title("🩻 Pneumonia Detector")

    # Navigation buttons
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("🔙 Back to Dashboard", key="back_dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()
    with col2:
        if st.button("🔓 Logout", key="logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()

    st.markdown("---")

    # Patient Information
    with st.expander("🧑‍⚕️ Enter Patient Information", expanded=True):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        st.session_state.patient_name = name
        st.session_state.patient_age = age
        st.session_state.patient_gender = gender

    # Upload or Camera
    mode = st.radio("Select Image Input Method", ["Upload Image", "Use Camera"])
    uploaded_image = None

    if mode == "Upload Image":
        uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            uploaded_image = Image.open(uploaded_file).convert("RGB")
            st.image(uploaded_image, caption="Uploaded X-ray Image", use_container_width=True)

    else:
        st.info("📸 Please take the picture of the X-ray in **good lighting** and ensure the full image is visible.")
        captured_image = st.camera_input("Capture Chest X-ray")
        if captured_image:
            uploaded_image = Image.open(captured_image).convert("RGB")
            st.image(uploaded_image, caption="Captured X-ray Image", use_container_width=True)

    model = load_model("models/T-ResNet.pth")

    

    if st.button("Analyze"):
            label, confidence = predict_image(uploaded_image, model)

            st.markdown(f"## 🩺 Prediction Result: **{label}**")
            st.markdown(f"### 📊 Confidence: **{confidence*100:.2f}%**")

            # Medical Report
            st.markdown("## 📝 Medical Report")
            st.markdown(f"**Patient Name:** {name}  \n"
                        f"**Age:** {age}  \n"
                        f"**Gender:** {gender}  \n"
                        f"**Diagnosis:** **{label}**")

            disease_info = {
                "Normal": """
                ### ✅ Diagnosis Summary

                No signs of Pneumonia or related lung infections.

                **Recommendations:**
                - Maintain regular health check-ups.
                - Continue a healthy lifestyle.
                """,

                "Pneumonia": """
                ### 🫁 Pneumonia Detected

                **Medical Advice:**
                - Consult a pulmonologist immediately.
                - Ensure complete rest and take medications as prescribed.
                - Stay hydrated and monitor symptoms.

                **Preventive Tips:**
                - Avoid exposure to cold air and infected individuals.
                """,

                "Viral Pneumonia": """
                ### 🦠 Viral Pneumonia Detected

                **Medical Advice:**
                - Isolation is recommended to prevent spread.
                - Follow antiviral treatment as advised.
                - Regular temperature and oxygen monitoring.

                **Social Message:**
                - Inform family members and take precautions to limit exposure.
                """,

                "Bacterial Pneumonia": """
                ### 🧫 Bacterial Pneumonia Detected

                **Medical Advice:**
                - Antibiotic treatment is required.
                - Avoid public places and ensure rest.
                - Complete the medication course.

                **Preventive Tips:**
                - Consider pneumococcal vaccines.
                - Regular health monitoring.
                """
            }

            st.markdown(disease_info.get(label, ""))
