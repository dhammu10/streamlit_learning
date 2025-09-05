import streamlit as st
import datetime

st.title("Age Calculater")
# st.subheader("Welcome Language Picker")
# lang = st.selectbox("Select Language", ["None", "Java", "C++", "Python", "JavaScript"])
# st.write(f"your Selected Language: {lang}")

# st.success(f"your selected language : {lang}") 

# masala = st.button("Add Masala")
# if masala:
#     st.success("Adding Masala")


# gender = st.radio("select gender: ", ["Male", "Female", "Other"])

# st.slider('give rating', 0, 10, 1)

# st.text_input("Enter Your name")
# st.number_input("Enter your age")
# st.date_input("select your birth day")


user_date = st.date_input("Enter Your age")
current_date = datetime.date.today()

user_age = current_date.year - user_date.year

st.success(f"your age is {user_age}")