import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "kilometers": {"meters": 1000, "centimeters": 100000, "miles": 0.621371},
        "meters": {"kilometers": 0.001, "centimeters": 100, "miles": 0.000621371},
        "centimeters": {"kilometers": 0.00001, "meters": 0.01, "miles": 0.0000062137},
        "miles": {"kilometers": 1.60934, "meters": 1609.34, "centimeters": 160934}
    }
    
    if from_unit == to_unit:
        return value
    
    return value * conversion_factors[from_unit][to_unit]

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #141E30, #243B55);
        color: white;
        font-family: 'Arial', sans-serif;
    }
    .stButton > button {
        background-color: #4CAF50;
        border: 2px solid #66BB6A;
        border-radius: 8px;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #388E3C;
        border-color: white;
        color: white;
    }
    .stSelectbox, .stTextInput, .stNumberInput {
        background-color: #222;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(to top, #4CAF50, #66BB6A);
        color: white !important;
    }
    .result-box {
        background-color: #333;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Unit Converter")

value = st.number_input("Enter the value:", min_value=0.0, format="%.4f")
units = ["kilometers", "meters", "centimeters", "miles"]
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.markdown(f"""
        <div class='result-box'>
            {value} {from_unit} is equal to {result:.4f} {to_unit}
        </div>
    """, unsafe_allow_html=True)
