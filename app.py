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
# PREMIUM CSS
# ============================

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
background: linear-gradient(120deg,#141E30,#243B55);
}

.card {
background: rgba(255,255,255,0.12);
padding:25px;
border-radius:20px;
box-shadow:0 0 25px rgba(0,255,255,0.4);
}

h1{
color:#00fff0;
text-align:center;
font-size:45px;
}

h3{
color:#ff9ff3;
text-align:center;
}

label{
color:white !important;
font-weight:bold;
}

.stButton>button{
background:linear-gradient(45deg,#00f260,#0575e6,#ff00cc);
color:white;
border-radius:30px;
height:3.2em;
width:100%;
font-size:22px;
font-weight:bold;
border:none;
box-shadow:0 0 25px #00f260;
}

.stButton>button:hover{
background:linear-gradient(45deg,#fc466b,#3f5efb);
}

.success{
background:linear-gradient(45deg,#11998e,#38ef7d);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
font-size:24px;
}

.danger{
background:linear-gradient(45deg,#ff416c,#ff4b2b);
padding:18px;
border-radius:15px;
text-align:center;
color:white;
font-size:24px;
}

</style>
""", unsafe_allow_html=True)

# ============================
# Title
# ============================

st.markdown("<h1>🍄 Mushroom AI Classifier</h1>", unsafe_allow_html=True)
st.markdown("<h3>Edible vs Poisonous Prediction</h3>", unsafe_allow_html=True)

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

cap_diameter = st.number_input("Cap Diameter (0 - 50)", 0.0, 50.0)
stem_height = st.number_input("Stem Height (0 - 50)", 0.0, 50.0)
stem_width = st.number_input("Stem Width (0 - 20)", 0.0, 20.0)

cap_shape = st.selectbox("Cap Shape", cap_shape_map.keys())
gill_attachment = st.selectbox("Gill Attachment", gill_attach_map.keys())
gill_color = st.selectbox("Gill Color", gill_color_map.keys())
stem_color = st.selectbox("Stem Color", stem_color_map.keys())
season = st.selectbox("Season", season_map.keys())

st.markdown("</div>", unsafe_allow_html=True)

# ============================
# Validate & Convert
# ============================

input_data = np.array([[
float(cap_diameter),
cap_shape_map[cap_shape],
gill_attach_map[gill_attachment],
gill_color_map[gill_color],
float(stem_height),
float(stem_width),
stem_color_map[stem_color],
season_map[season]
]])

# ============================
# Prediction
# ============================

if st.button("🚀 Predict Mushroom Type"):
    try:
        pred = model.predict(input_data)[0]

        if pred == 0:
            st.markdown("<div class='success'>✅ EDIBLE MUSHROOM</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='danger'>☠️ POISONOUS MUSHROOM</div>", unsafe_allow_html=True)

    except:
        st.error("⚠️ Please enter valid values in all fields")

# ============================
# Footer
# ============================

st.markdown("<p style='text-align:center;color:#aaa;'>Developed by Govarthanan</p>", unsafe_allow_html=True)
