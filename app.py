import streamlit as st

st.title("Website")

fn,ln = st.columns(2)

first_name = fn.text_input(label="First Name")

last_name = ln.text_input(label="Last Name")

em,pwd = st.columns(2)

email = em.text_input("Email")

password = pwd.text_input("Password",type="password")


if st.button(label="Submit"):
    st.balloons()