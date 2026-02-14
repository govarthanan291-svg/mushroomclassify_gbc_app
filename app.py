import streamlit as st
import numpy as np
import joblib

# ============================
# Page Config
# ============================

st.set_page_config(
    page_title="Mushroom AI Classifier",
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
# ADVANCED PREMIUM CSS
# ============================

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
background: linear-gradient(120deg, #0f0c29, #302b63, #24243e);
}

.card {
background: rgba(255,255,255,0.12);
backdrop-filter: blur(12px);
padding: 25px;
border-radius: 20px;
box-shadow: 0 0 25px rgba(0,255,255,0.4);
margin-bottom:20px;
}

h1 {
color:#00f7ff;
text-align:center;
font-size:48px;
text-shadow:0 0 15px #00f7ff;
}

h3 {
color:#ff61d2;
text-align:center;
}

label {
color:white !important;
font-weight:bold;
}

.stButton > button {
background: linear-gradient(45deg,#00f260,#0575e6,#ff00cc);
color:white;
border-radius:30px;
height:3.2em;
width:100%;
font-size:22px;
font-weight:bold;
border:none;
box-shadow:0 0 25px #00f260;
}

.stButton > button:hover {
background: linear-gradient(45deg,#fc466b,#3f5efb);
box-shadow:0 0 30px #fc466b;
}

input {
border-radius:12px !important;
}

.success-box {
background: linear-gradient(45deg,#00b09b,#96c93d);
padding:20px;
border-radius:15px;
color:white;
font-size:24px;
text-align:center;
font-weight:bold;
box-shadow:0 0 20px #00b09b;
}

.danger-box {
background: linear-gradient(45deg,#ff416c,#ff4b2b);
padding:20px;
border-radius:15px;
color:white;
font-size:24px;
text-align:center;
font-weight:bold;
box-shadow:0 0 20px #ff416c;
}

</style>
""", unsafe_allow_html=True)

# ============================
# Title
# ============================

st.markdown("<h1>🍄 Mushroom AI Classifier</h1>", unsafe_allow_html=True)
st.markdown("<h3>Smart Prediction System</h3>", unsafe_allow_html=True)

# ============================
# Mappings
# ============================

cap_shape_map = {"Bell":0,"Conical":1,"Flat":2,"Convex":3}
gill_attach_map = {"Free":0,"Attached":1}
gill_color_map = {"White":0,"Brown":1,"Gray":2,"Pink":3}
stem_color_map = {"White":0,"Brown":1,"Yellow":2,"Gray":3}
season_map = {"Spring":0,"Summer":1,"Autumn":2,"Winter":3}

# ============================
# Input Card
# ============================

st.markdown("<div class='card'>", unsafe_allow_html=True)

cap_diameter = st.number_input("Cap Diameter")
cap_shape = st.selectbox("Cap Shape", cap_shape_map.keys())
gill_attachment = st.selectbox("Gill Attachment", gill_attach_map.keys())
gill_color = st.selectbox("Gill Color", gill_color_map.keys())
stem_height = st.number_input("Stem Height")
stem_width = st.number_input("Stem Width")
stem_color = st.selectbox("Stem Color", stem_color_map.keys())
season = st.selectbox("Season", season_map.keys())

st.markdown("</div>", unsafe_allow_html=True)

# ============================
# Convert
# ============================

input_data = np.array([[
cap_diameter,
cap_shape_map[cap_shape],
gill_attach_map[gill_attachment],
gill_color_map[gill_color],
stem_height,
stem_width,
stem_color_map[stem_color],
season_map[season]
]])

# ============================
# Prediction
# ============================

if st.button("🚀 Predict Mushroom Type"):
    pred = model.predict(input_data)[0]

    if pred == 0:
        st.markdown("<div class='success-box'>✅ EDIBLE MUSHROOM</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='danger-box'>☠️ POISONOUS MUSHROOM</div>", unsafe_allow_html=True)

# ============================
# Footer
# ============================

st.markdown("<p style='text-align:center;color:#aaa;'>Developed by Govarthanan</p>", unsafe_allow_html=True)
