import streamlit as st

st.set_page_config(page_title="BMI Calculator",page_icon="📊",layout="centered")
st.title("🧘🏻‍♀️ BMI Calculator")
st.write("Let's Calculate Your **BODY MASS INDEX [BMI]** and Understand What It Means")

st.header("🖋 Enter Your Details")

height = st.number_input("Enter Your Height (in cm)",min_value=90,max_value=200,value=170)
weight = st.number_input("Enter Your Weight (in kg)",min_value=10,max_value=200,value=65)

st.write(f"🕺🏼 Your Height : {height} in cm")
st.write(f"🤸🏼 Your Weight : {weight} in kg")

if st.button("Calculate BMI"):
    h_m = height / 100               # converting cm to meters
    bmi = weight / (h_m**2)          # calculating the BMI
    st.success(f"YOUR BMI IS **{bmi :.2f}**")

    # Print BMI Category
    if bmi < 18.5:
        category = "Underweight 😞"
        color = "#9C3FDE"

    elif 18.5 <= bmi < 25:
        category = "Normal BodyWeight 😁"
        color = "#DE3FD1"

    elif 25 <= bmi < 30:
        category = "Overweight 😫"
        color = "#DE3F81"

    else:
        category = "Obese 😵"
        color = "#6056C8"

    st.markdown(
        f"""
        <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
        <h3>Your BMI Category : {category}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )