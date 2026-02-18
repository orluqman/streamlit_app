

import joblib
import numpy as np
import streamlit as st

#load trained model
model = joblib.load(r"models\wastewater_model.pkl")

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Wastewater Prediction System",
    layout="wide",
)

# # --- CUSTOM CSS ---
# st.markdown("""
# <style>
# /* Hide Streamlit default menu, footer, and header */
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}

# /* App background */
# [data-testid="stAppViewContainer"] {
#     background: linear-gradient(to right, #e0f7fa, #ffffff);
# }
# /* Dashboard card */
# .dashboard-card {
#       background: white;
#       padding: 32px;
#       border-radius:16px;
#       box-shadow: 0 12px 30px rgba(0,0,0,0.08);
#       max-width: 850px;
#       margin: auto;                                               
#        }


# /* title */
#   .dashboard-title {
#        font-size: 26px;
#         font-weight: 700;
#         margin-bottom: 8px;
#         color: #0f172a;                          
# }

#   /* Subtitle */  
#    .dashboard-subtitle{
#             font-size: 15px;
#             color: #64748b;
#             margin-bottom: 28px;
#      }                 
# /* Header */
# .header {
#     background-color: #00796B;
#     padding: 20px;
#     border-radius: 10px;
#     text-align: center;
#     color: white;
#     font-size: 36px;
#     font-weight: bold;
#     box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
# }

# /* Input boxes */
# .stNumberInput > div > input {
#     border-radius: 8px;
#     border: 1px solid #00796B;
#     padding: 8px;
# }

# /* input label styling */
#     label {
#         font-size: 16px !important;
#         font-weight: 600 !important;
#         color: #0ea5e9 !important;    /* blue professional */           
#      }      

#     /* Make labels stand out slightly more */
#       div[data-testid="stNumberInput"] label {
#         margin-bottom: 6px   
#      }                           
# /* Buttons */
# div.stButton > button {
#     background-color: #009688;
#     color: white;
#     border-radius: 8px;
#     height: 3em;
#     width: 100%;
#     font-size: 16px;
#     border: none;
#     font-weight: bold;
# }

# div.stButton > button:hover {
#     background-color: #00796B;
#     color: white;
# }

#   /*Inputs spacing*/
#    div[data-baseweb="input"] {
#     margin-bottom: 15px;
#      }  

#   /* Balanced input width */
#      div[data-baseweb="input"] > div {
#         display: flex;
#         max-width: 320px;       
#        min-width: 260px; 
#     }        
     
#  /* improve input height */
#      div[data-baseweb="input"] input {
#         height: 42px    
#     }                                                       
# /* Footer */
# .footer {
#     text-align: center;
#     padding: 10px;
#     background-color: #004D40;
#     color: white;
#     border-radius: 10px;
#     margin-top: 20px;
#     font-size: 14px;
# }
# </style>
# """, unsafe_allow_html=True)


st.markdown("""
<style>
/* ===== Government theme ===== */
.stApp {
    background-color: #f1f5f9;
    font-family: "Segoe UI", Arial, sans-serif;
}

/* Header bar */
.gov-header {
    background: #0f172a;
    color: white;
    padding: 16px 24px;
    border-radius: 10px;
    margin-bottom: 24px;
}

.gov-title {
    font-size: 22px;
    font-weight: 700;
}

.gov-subtitle {
    font-size: 14px;
    color: #cbd5f5;
}

/* Card */
.dashboard-card {
    border: 1px solid #cbd5e1;
    box-shadow: none;
    border-radius: 8px;
}

/* Section title */
.gov-section {
    font-size: 15px;
    font-weight: 700;
    color: #1f2937;
    border-bottom: 2px solid #e5e7eb;
    padding-bottom: 6px;
    margin: 20px 0 16px 0;
}

/* Labels */
label {
    font-size: 15px !important;
    font-weight: 700 !important;
    color: #1e3a8a !important;  /* gov blue */
}

/* Inputs */
div[data-baseweb="input"] > div {
    min-width: 280px;
    max-width: 340px;
}
div[data-baseweb="input"] input {
    height: 44px;
    border-radius: 6px;
    border: 1px solid #94a3b8;
}

/* Button */
div.stButton > button {
    background: #1e3a8a;
    border-radius: 6px;
    font-size: 16px;
}
div.stButton > button:hover {
    background: #1d4ed8;
}
</style>
""", unsafe_allow_html=True)



# --- HEADER ---
st.markdown('<div class="header">Wastewater Volume Prediction System 💧</div>', unsafe_allow_html=True)
st.markdown('<div class="dashboard-card">',unsafe_allow_html=True)

st.markdown('<div class="dashboard-title"> Wastewater Prediction Dashboard</div>',unsafe_allow_html=True)
st.markdown('<div class="dashboard-subtitle">Enter the system parameters to estimate wastewater volume</div>'
            ,unsafe_allow_html=True)

#-----------ROW 1----------------------
col1, col2 = st.columns(2)

with col1 :
    population = st.number_input("👭 Population",min_value=0.0, value=None)
    
    with col2:
     rainfall = st.number_input("Rainfall (mm)",min_value=0.0,value=None)  


     #------------ROW 2--------------

col3, col4 =st.columns(2)
with col3:
   avg_domestic_water_use =st.number_input("Domestic water use (L/day)",min_value=0.0,value=None) 

with col4:
   industrial_water_use = st.number_input("Industrial water use (L/day)",min_value=0.0,value=None)   

# --- INPUTS ---
#st.markdown('<div class="section-title">Enter details below:</div>',unsafe_allow_html=True)

#---------------ROW 3 (CENTRED)-----------------
col5, col6, col7 = st.columns([1, 2, 1])
with col6:
   sewer_connection_rate = st.number_input("Sewer connection rate(%)",min_value=0.0, max_value=100.0 ,value=None)

   st.markdown("---")
# --- BUTTON ---
if st.button("Predict Wastewater Volume"):
    input_data = [[
        population,
        rainfall,
        avg_domestic_water_use,
        industrial_water_use,
        sewer_connection_rate,
    ]]
    predict = model.predict(input_data)[0]
    # Dummy prediction for now
    
    st.success(f"💧 Predicted Wastewater Volume: {predict:.2f} m³")
st.markdown('</div>',unsafe_allow_html=True)
# --- FOOTER ---
st.markdown('<div class="footer">© 2026 Ministry of Water Resources | Data is confidential</div>', unsafe_allow_html=True)


#load trained model
#model = joblib.load(r"models\wastewater_model.pkl")
