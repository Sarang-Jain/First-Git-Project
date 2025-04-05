import streamlit as st
import pandas as pd
import numpy as np


st.title("Welcome to Mayfair")
st.write("Please start your hotel booking")

name=st.text_input("Enter Your Name")
if name:
    st.write(f"Hello, {name}")

room=["Normal","Delux","Executive"]
Selectedroom=st.selectbox("Select your preferred room", room, index=None)
st.write(f"Your Preference : {Selectedroom}")

def roomchoice(Selectedroom):
    if Selectedroom=="Normal":
        st.write("Normal room selected. Cost approx 5000")
    elif Selectedroom=="Delux":
        st.write("Delux room selected. Cost approx 6000")
    elif Selectedroom=="Executive":
        st.write("Delux room selected. Cost approx 7000")

roomchoice(Selectedroom)

from datetime import datetime, tzinfo

startdate= st.slider("Start date",value=datetime(2025,5,1), format="MM/DD/YY")
st.write(f"Your Start Date:{startdate}")

enddate= st.slider("End date",value=datetime(2025,5,1,9,30), format="MM/DD/YY-hh:mm:ss")
st.write(f"Your End Date:{enddate}")

Instruction=st.text_input("Note: Any instruction before checkin")
if Instruction:
    st.write(f"Your Instruction is noted")

submission=st.button("Submit")
if submission:
    st.write("Congratulations, your booking is confirm")
