import streamlit as st

number1 = st.number_input('Insert first number')
number2 = st.number_input('Insert second number')
number3 = st.number_input('Insert third number')
number = max(number1, number2, number3)
st.write('The largest number is ', number)
