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
# CSS STYLE
# ============================

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

h1, h2, h3, h4, label, span {
color: white !important;
text-align:center;
}

.stButton > button {
background: linear-gradient(45deg,#ff416c,#ff4b2b);
color:white;
border-radius:25px;
height:3em;
width:100%;
font-size:20px;
font-weight:bold;
}

.stButton > button:hover {
background: linear-gradient(45deg,#11998e,#38ef7d);
}

</style>
""", unsafe_allow_html=True)

# ============================
# Title
# ============================

st.markdown("<h1>🍄 Mushroom Classification App</h1>", unsafe_allow_html=True)
st.markdown("<h3>Edible vs Poisonous Prediction</h3>", unsafe_allow_html=True)

# ============================
# MAPPINGS
# ============================

cap_shape_map = {"Bell":0, "Conical":1, "Flat":2, "Convex":3}
gill_attach_map = {"Free":0, "Attached":1}
gill_color_map = {"White":0, "Brown":1, "Gray":2, "Pink":3}
stem_color_map = {"White":0, "Brown":1, "Yellow":2, "Gray":3}
season_map = {"Spring":0, "Summer":1, "Autumn":2, "Winter":3}

# ============================
# INPUTS
# ============================

cap_diameter = st.number_input("Cap Diameter")

cap_shape = st.selectbox("Cap Shape", list(cap_shape_map.keys()))
gill_attachment = st.selectbox("Gill Attachment", list(gill_attach_map.keys()))
gill_color = st.selectbox("Gill Color", list(gill_color_map.keys()))
stem_height = st.number_input("Stem Height")
stem_width = st.number_input("Stem Width")
stem_color = st.selectbox("Stem Color", list(stem_color_map.keys()))
season = st.selectbox("Season", list(season_map.keys()))

# Convert to numeric
cap_shape_val = cap_shape_map[cap_shape]
gill_attach_val = gill_attach_map[gill_attachment]
gill_color_val = gill_color_map[gill_color]
stem_color_val = stem_color_map[stem_color]
season_val = season_map[season]

# ============================
# Prediction
# ============================

if st.button("Predict Mushroom Type 🍄"):
    input_data = np.array([[cap_diameter,
                             cap_shape_val,
                             gill_attach_val,
                             gill_color_val,
                             stem_height,
                             stem_width,
                             stem_color_val,
                             season_val]])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("✅ EDIBLE MUSHROOM")
    else:
        st.error("☠️ POISONOUS MUSHROOM")

# ============================
# Footer
# ============================

st.markdown("<p style='text-align:center;color:white;'>Developed by Govarthanan</p>", unsafe_allow_html=True)
