import streamlit as st

st.title(" Food Delivery App")

name = st.text_input("Enter Your Name")

food = st.selectbox(
    "Choose Your Food",
    ["Pizza ", "Burger ", "Sandwich ", "Pasta "]
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    max_value=10,
    value=1
)

if st.button("Place Order"):
    st.success(
        f"Thank You {name}! Your order for {quantity} {food} has been placed successfully.")
