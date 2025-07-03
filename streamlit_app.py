import streamlit as st
import requests
from urllib.parse import urljoin


API_BASE_URL_RENDER = "https://test-api-j3rz.onrender.com"
API_ENDPOINT_SALARY = "/salary"

st.title("Salary Calculator")
st.markdown("*Using API hosted on render.com*")

st.subheader("Input:")

salary = st.number_input("Salary", value=2500)
bonus = st.number_input("Bonus", value=200)
taxes = st.number_input("Taxes", value=400)

if st.button("Calculate"):
    url = urljoin(API_BASE_URL_RENDER, API_ENDPOINT_SALARY)

    response = requests.post(
        url, json={"salary": salary, "bonus": bonus, "taxes": taxes}
    )

    if response.status_code == 200:
        st.success(f"Net salary: {response.json()['result']}")
    else:
        st.error("API error: " + response.text)
