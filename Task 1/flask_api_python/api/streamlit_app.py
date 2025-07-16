import streamlit as st
import requests


API_URL = "http://localhost:5000/predict"
iris_classes = ["Setosa 🌱", "Versicolor 🌼", "Virginica 🌺"]


st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")


with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg", caption="Iris Flower")
    st.markdown("### 👋 Welcome to Iris Classifier!")
    st.markdown("This app uses a **Random Forest** model served by a Flask API to classify Iris flowers based on:")
    st.markdown("- Sepal Length\n- Sepal Width\n- Petal Length\n- Petal Width")


st.title("🌸 Iris Flower Classifier")
st.write("Fill in the flower's features to predict its species:")


col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("🌿 Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1, step=0.1)
    petal_length = st.number_input("🌼 Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4, step=0.1)

with col2:
    sepal_width = st.number_input("🌿 Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
    petal_width = st.number_input("🌼 Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

st.markdown("---")


if st.button("🔍 Predict Flower Type"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    payload = {"feature_array": features}

    with st.spinner("Sending data to the model..."):
        try:
            response = requests.post(API_URL, json=payload)
            result = response.json()

            if "prediction" in result:
                class_index = result["prediction"][0]
                st.success(f"🎉 The predicted flower is: **{iris_classes[class_index]}** (Class {class_index})")
            else:
                st.error(f" API returned an error: {result.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f" Could not connect to API: `{e}`")


