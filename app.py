import streamlit as st

st.title("Hello Dhammdip")
st.subheader("Welcome Language Picker")
lang = st.selectbox("Select Language", ["None", "Java", "C++", "Python", "JavaScript"])
st.write(f"your Selected Language: {lang}")

st.success(f"your selected language : {lang}") 