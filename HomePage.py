import streamlit as st
import Analyser as ast
import Covid19_Data2 as cvd
sel = st.sidebar.selectbox("Select as per requirement: ",["Home Page","COVID-19"])
st.write("# WELCOME TO HEALTHCARE SYSTEM")
st.write("## This web app is incomplete")
st.write("Choose from options on left")
if(sel == "COVID-19"):
    sel2 = st.sidebar.radio("SELECT: ",["Prediction","Covid Cases Comparator","Visual Analyser"])
    if(sel2 == "Visual Analyser"):
        st.write("** Close the navigation bar on left for better experience **")
        ast.race()
    elif("Covid Cases Comparator"):
        cvd.CovidCases()
    else:
        pass
else:
    pass
