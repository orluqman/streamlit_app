

import joblib
import numpy as np
import streamlit as st

import streamlit as st
import numpy as np
import base64

st.set_page_config(
    page_title="Wastewater Prediction App",
    layout="wide"
)

# ----------- FUNCTION YA KUWEKA BACKGROUND IMAGE -----------
#def set_bg(image_file):
  #  with open(image_file, "rb") as file:
    #    encoded = base64.b64encode(file.read()).decode()
#st.markdown(f"""
 #   <style>
  #  .stApp {{
      #  background-image: url("data:image/jpg;base64,{encoded}");
      #  background-size: cover;
       # background-position: center;
       # background-attachment: fixed;
 #   }}
 #   </style>
 #   """, unsafe_allow_html=True)

# 👉 Weka jina la picha yako hapa (iwe kwenye folder moja na app.py)
#set_bg("background.jpg")


# ----------- CUSTOM CSS -----------
st.markdown("""
<style>

/* Glass effect container */
.block-container {
    background: rgba(255,255,255,0.85);
    padding: 2rem;
    border-radius: 15px;
}

/* Header */
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #1B4F72;
    text-align: center;
    margin-bottom: 10px;
}

.sub-text {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Input styling */
div[data-baseweb="input"] > div {
    border-radius: 10px !important;
    border: 2px solid #2E86C1 !important;
}

/* Button */
div.stButton > button {
    background-color: #2E86C1;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

div.stButton > button:hover {
    background-color: #154360;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ----------- HEADER -----------
st.markdown('<div class="main-title">💧 Wastewater Volume Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Enter ward details below</div>', unsafe_allow_html=True)

# ----------- INPUT COLUMNS -----------
col1, col2, col3 = st.columns(3)

with col1:
    population = st.number_input("Population", min_value=0)

with col2:
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

with col3:
    households = st.number_input("Households", min_value=0)

st.markdown("<br>", unsafe_allow_html=True)

# ----------- SINGLE PREDICT BUTTON -----------
if st.button("Predict Wastewater Volume"):
    prediction = population * 0.2 + rainfall * 1.5 + households * 0.5
    st.success(f"Predicted Wastewater Volume: {prediction:,.2f} Liters")



#load trained model
#model = joblib.load(r"models\wastewater_model.pkl")

#st.title("Wastewater Volume Prediction App")

#user input
#total_population = st.number_input("Enter total population",
                               #    min_value=0.0,
                                 #  value=None,
                                  # placeholder="eg3000")

#avg_domestic_water_use = st.number_input("Enter domestic water usage",
                                        #  min_value=0.0,
                              #     value=None,
                               #    placeholder="eg3000")

#industrial_water_use = st.number_input("Enter industrial water use",
      #                                  min_value=0.0,
      #                             value=None,
      #                             placeholder="eg3000")

#sewer_connection_rate = st.number_input("Enter sewer connection rate",
            #                             min_value=0.0,
             #                      value=None,
            #                       placeholder="eg3000")

#rainfall_mm = st.number_input("Enter amount of rainfall (mm)",
#min_value=0.0,
                     #              value=None,
                         #          placeholder="eg3000")

#if st.button("Predict"):
 #   input_data = np.array([[total_population ,avg_domestic_water_use , industrial_water_use , sewer_connection_rate ,rainfall_mm]])
  #  prediction = model.predict(input_data)

  #  st.success(f"Predicted Wastewater Volume:{prediction[0]}")




