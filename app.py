import streamlit as st
import numpy as np
import joblib

# ============================
# Page Config
# ============================

st.set_page_config(
    page_title="Mushroom Classifier",
    page_icon="🍄",
    layout="centered"
)

# ============================
# Load Model
# ============================

@st.cache_resource
def load_model():
    return joblib.load("mushroom_gb_model.pkl")

model = load_model()

# ============================
# Dark Green Theme CSS
# ============================

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #0b3d2e;
}

[data-testid="stHeader"] {
    background-color: #0b3d2e;
}

[data-testid="stSidebar"] {
    background-color: #0b3d2e;
}

h1, h2, h3, h4, label, span, p {
    color: #e6ffe6 !important;
}

.stButton > button {
    background-color: #1f7a4d;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.stButton > button:hover {
    background-color: #145a32;
}

input {
    background-color: #145a32 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ============================
# Title
# ============================

st.markdown("<h1 style='text-align:center;'>🍄 Mushroom Classification App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Predict Edible or Poisonous</h4>", unsafe_allow_html=True)

# ============================
# Input Fields
# ============================

cap_diameter = st.number_input("Cap Diameter", min_value=0.0)
cap_shape = st.number_input("Cap Shape (Encoded)", min_value=0)
gill_attachment = st.number_input("Gill Attachment (Encoded)", min_value=0)
gill_color = st.number_input("Gill Color (Encoded)", min_value=0)
stem_height = st.number_input("Stem Height", min_value=0.0)
stem_width = st.number_input("Stem Width", min_value=0.0)
stem_color = st.number_input("Stem Color (Encoded)", min_value=0)
season = st.number_input("Season (Encoded)", min_value=0.0)

# ============================
# Prediction
# ============================

if st.button("Predict Mushroom Type"):
    input_data = np.array([[cap_diameter, cap_shape, gill_attachment,
                             gill_color, stem_height, stem_width,
                             stem_color, season]])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("✅ This Mushroom is EDIBLE")
    else:
        st.error("☠️ This Mushroom is POISONOUS")

# ============================
# Footer
# ============================

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Developed by Govarthanan</p>", unsafe_allow_html=True)
