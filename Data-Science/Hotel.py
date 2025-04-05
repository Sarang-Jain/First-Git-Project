import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to Mayfair")
st.write("Please start your hotel booking")

# Input for user's name
name = st.text_input("Enter Your Name")
if name:
    st.write(f"Hello, {name}")

# Room options
room = ["Normal", "Delux", "Executive"]
Selectedroom = st.selectbox("Select your preferred room", room, index=None)
st.write(f"Your Preference: {Selectedroom}")

# Function to display room choice and cost
def roomchoice(Selectedroom):
    if Selectedroom == "Normal":
        st.write("Normal room selected. Cost approx 5000")
    elif Selectedroom == "Delux":
        st.write("Delux room selected. Cost approx 6000")
    elif Selectedroom == "Executive":
        st.write("Executive room selected. Cost approx 8000")

# Call the function with the selected room
roomchoice(Selectedroom)