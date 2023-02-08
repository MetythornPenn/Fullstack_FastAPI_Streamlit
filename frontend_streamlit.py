# import the important libraries
import streamlit as st
import requests
import json

def run():
    st.title("Full Stack ML App using FastAPI and Streamlit")
    st.write("This is a simple example of how to use the streamlit option menu")
    name = st.text_input("Name")
    year = st.number_input("Year of Experience", min_value=0, max_value=100, value=0, step=1)
    

    data = {
        "year": year
    }

    if st.button("Predict"):
        response = requests.post("http://localhost:8000/predict", json=data)
        json = response.json()
        prediction_json = json.get("year")
        prediction = prediction_json.get("0")
        st.success(f"Hi {name}")
        st.success(f"Your salary is {prediction}")


        

if __name__ == "__main__":
    # by default streamlit runs on port 8501
    run()