import streamlit as st
import datetime as dt

st.title("Welcome to school portal")
st.header("Registration")
st.text("Please fill in your details accurately")
fn = st.text_input("Enter your first name")
ln = st.text_input("Enter your last name")
nationality =st.text_input("What is your nationality")
state = st.text_input("What is your state")
LGA = st.text_input("What is your LGA")
DOB = st.date_input("Select your date of birth", min_value=dt.datetime(1850,1,1), format="DD/MM/YYYY")

st.write(f'First name = {fn}')
st.write(f"Last name ={ln}")
st.write(f"Your country is = {nationality}")
st.write(f"Your state is {state}")
st.write(f"Your Local Government Area is = {LGA}")
st.write(f"Your date of birth is = {DOB}")

changes = st.radio("Do you want to make any changes ?",('Yes','No'))
if changes == 'yes':
    change = st.text_input("Where do you want to make changes")
    if change == 'first name':
        fn = st.text_input("What would you like to be your first name")
    elif change == 'last name':
        ln = st.text_input("What would you like to be your last name")
    elif change == 'nationality':
        nationality = st.text_input("What do you want to be your new nationality")
    elif change == "state":
        state = st.text_input("What do you want to be your new state")
    elif change == 'LGA':
        LGA= st.text_input("What do you want to be your LGA")
    elif change =='DOB':
        DOB = st.text_input("What do you want to be your DOB")
    else:
        st.write('Write the spellings as follows')
        st.write('first name')
        st.write('last name')
        st.write('nationality')
        st.write('state')
        st.write('LGA')
        st.write('DOB')
    st.write("This is your profile")
    st.write(fn)
    st.write(ln)
    st.write(nationality)
    st.write(state)
    st.write(LGA)
    st.write(DOB)
else:
    st.write('This is your profile')
    st.write(f'First name = {fn}')
    st.write(f"Last name = {ln}")
    st.write(f"Your country is = {nationality}")
    st.write(f"Your state is {state}")
    st.write(f"Your Local Government Area is = {LGA}")
    st.write(f"Your date of birth is = {DOB}")