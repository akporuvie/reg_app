import streamlit as st
import datetime as dt

st.title("Welcome to school portal")
st.header("Registration")
st.text("Please fill in your details accurately")
fn = st.text_input("Enter your first name")
ln = st.text_input("Enter your last name")
dob = st.date_input("Select your date of birth", min_value=dt.datetime(1850,1,1), format="DD/MM/YYYY")
gender = st.selectbox("Select your gender",['male','female'])
race = st.radio("Seluct your race",('White','Black','Asian'))
if st.checkbox("Ready to submit ?"):
    st.write(f"You are a {race} {gender}")
if st.button('Submit'):
    st.success("Submitted Successfully")
    # st.error("Something went wrong")
    # st.warning("Warning")
    # st.info("This is for your information")