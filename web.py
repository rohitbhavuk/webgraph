import streamlit as st
import numpy as np
#import matplotlib.pyplot as plt
import plotly.express as pe
st.title("Welcome to Rising Stars")
st.subheader("Power")
st.checkbox("testing")
x=st.number_input("Enter a Number",value=0,format="%d")
y=st.number_input("Enter Exponent",value=0,format="%d")
if st.button("Press Here"):
    result=x**y
    st.write(f"{x} power {y} is {result}")

st.title("Plotting graph")
x=st.number_input("Enter starting range",value=0,format="%d")
y=st.number_input("Enter last range",value=0,format="%d")
z=st.number_input("Enter power",value=0,format="%d")

if st.button("Graph"):
    x1=np.linspace(x,y,100)
    y1=[i**z for i in x1]
    fig=pe.line(x=x1,y=y1)
    st.plotly_chart(fig)
