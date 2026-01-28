import streamlit as st

st.title("Tali")

name = st.slider("This is a slider",1,100)
st.write(f"Output: {name}")


