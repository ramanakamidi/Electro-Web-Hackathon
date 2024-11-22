import streamlit as st
import math as mt
st.set_page_config(layout="wide", page_title="Transformer")

def Tran_Eff(v0,i0,w0):
    npf = w0/(v0*i0)
    iu = i0*(mt.sqrt(1-(npf)**2))
    iw = i0*npf
    r0 = v0/iw
    x0 = v0/iu
    return r0,x0


st.title("2205A21019-PS7")
st.write("Calculate the resistance (R0) and reactance (X0) of a transformer based on open circuit test measurements like V0,I0,W0.")
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        v0 = st.number_input("Enter Transformer Output Voltage (V0)", value=5.0,step=1.0)
        i0 = st.number_input("Enter Transformer Output Cutrrent (I0)", value=3.0 ,step=1.0)
        w0 = st.number_input("Enter power (W0)", value=1.0 ,step=1.0)

with col2:
    with st.container(border=True):
        r0, x0 = Tran_Eff(v0,i0,w0)
        st.write("Transformer function Results:")
        st.write(f"Resistance (R0) = {r0:.2f} Ohms")
        st.write(f"Reactance (X0) = {x0:.2f} Ohms")