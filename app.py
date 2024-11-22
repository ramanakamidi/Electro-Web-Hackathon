import streamlit as st
import math as mt

# Streamlit Page Configuration
st.set_page_config(layout="wide", page_title="Transformer")

# Transformer Efficiency Function
def Tran_Eff(v0, i0, w0):
    # Calculate Power Factor (npf), iu, and iw
    npf = w0 / (v0 * i0)
    iu = i0 * (mt.sqrt(1 - (npf)**2))
    iw = i0 * npf
    # Calculate Resistance (R0) and Reactance (X0)
    r0 = v0 / iw
    x0 = v0 / iu
    return r0, x0

# Page Title and Description
st.title("2205A21019-PS7")
st.write("Calculate the resistance (R0) and reactance (X0) of a transformer based on open circuit test measurements like V0, I0, W0.")

# Create two columns for input and output
col1, col2 = st.columns(2)

# First Column - Input Values
with col1:
    with st.container(border=True):
        v0 = st.number_input("Enter Transformer Output Voltage (V0)", value=5.0, step=1.0)
        i0 = st.number_input("Enter Transformer Output Current (I0)", value=3.0, step=1.0)
        w0 = st.number_input("Enter Power (W0)", value=1.0, step=1.0)
        calculate_button = st.button("Calculate")

# Second Column - Results
with col2:
    if calculate_button:
        # Perform calculations when button is clicked
        try:
            r0, x0 = Tran_Eff(v0, i0, w0)
            st.write("Transformer Function Results:")
            st.write(f"Resistance (R0) = {r0:.2f} Ohms")
            st.write(f"Reactance (X0) = {x0:.2f} Ohms")
        except Exception as e:
            st.write(f"Error in calculation: {e}")
