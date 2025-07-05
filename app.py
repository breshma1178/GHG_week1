import streamlit as st
import joblib
import numpy as np
import pandas as pd
from utils.preprocessor import preprocess_input

# ✅ Load model and scaler
model = joblib.load('models/LR_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# ✅ Basic page config
st.set_page_config(page_title="Supply Chain Emissions Prediction", page_icon="🌍")

# ✅ Add custom CSS
st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background-color: #f6f9f8;
        color: #333333;
    }

    /* Input widget container */
    .stForm {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* Title style */
    h1 {
        color: #004d40;
        font-family: 'Arial', sans-serif;
    }

    /* Button style */
    div.stButton > button:first-child {
        background-color: #004d40;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }

    div.stButton > button:hover {
        background-color: #00796b;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ App title
st.title("🌍 Supply Chain Emissions Predictor")

st.markdown("""
This app predicts **Supply Chain Emission Factors with Margins**  
based on DQ metrics and other parameters.
""")

# ✅ Input form
with st.form("prediction_form"):
    substance = st.selectbox("Substance", ['carbon dioxide', 'methane', 'nitrous oxide', 'other GHGs'])
    unit = st.selectbox("Unit", ['kg/2018 USD, purchaser price', 'kg CO2e/2018 USD, purchaser price'])
    source = st.selectbox("Source", ['Commodity', 'Industry'])
    supply_wo_margin = st.number_input("Supply Chain Emission Factors without Margins", min_value=0.0)
    margin = st.number_input("Margins of Supply Chain Emission Factors", min_value=0.0)
    dq_reliability = st.slider("DQ Reliability", 0.0, 1.0)
    dq_temporal = st.slider("DQ Temporal Correlation", 0.0, 1.0)
    dq_geo = st.slider("DQ Geographical Correlation", 0.0, 1.0)
    dq_tech = st.slider("DQ Technological Correlation", 0.0, 1.0)
    dq_data = st.slider("DQ Data Collection", 0.0, 1.0)

    submit = st.form_submit_button("🚀 Predict")

# ✅ Prediction
if submit:
    input_data = {
        'Substance': substance,
        'Unit': unit,
        'Supply Chain Emission Factors without Margins': supply_wo_margin,
        'Margins of Supply Chain Emission Factors': margin,
        'DQ ReliabilityScore of Factors without Margins': dq_reliability,
        'DQ TemporalCorrelation of Factors without Margins': dq_temporal,
        'DQ GeographicalCorrelation of Factors without Margins': dq_geo,
        'DQ TechnologicalCorrelation of Factors without Margins': dq_tech,
        'DQ DataCollection of Factors without Margins': dq_data,
        'Source': source,
    }

    input_df = preprocess_input(pd.DataFrame([input_data]))
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    st.success(f"✅ Predicted Supply Chain Emission Factor with Margin: **{prediction[0]:.4f}**")
