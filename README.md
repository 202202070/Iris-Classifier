# 🌸 Iris Classifier API & Streamlit App

This project is based on a clone of [AchilleasKn/flask_api_python](https://github.com/AchilleasKn/flask_api_python), and has been extended to build a machine learning pipeline for classifying **Iris flowers** using both a **Flask REST API** and a **Streamlit web app**.

---

## 🔁 Cloned From

> [https://github.com/AchilleasKn/flask_api_python](https://github.com/AchilleasKn/flask_api_python)

---

## ✅ Updates & Enhancements

After cloning, the following updates were made:

- ✅ Trained a **machine learning model** (using `Random Forrest Classifier`) on the **Iris dataset**.
- ✅ Modified the `/predict` Flask API endpoint to accept an array of four numerical features and return the Iris class.
- ✅ Added a **Streamlit interface** (`streamlit_app.py`) for a user-friendly way to interact with the model.
- ✅ Structured the project to work with **Docker** and **Docker Compose**.
- ✅ Improved code organization and project structure.

---

## 🧠 Tech Stack

- **Flask** – REST API
- **Streamlit** – Web-based UI
- **scikit-learn** – Model training and prediction
- **pickle** – Model serialization
- **Docker** & **Docker Compose** – Containerization
- **Postman** – API testing

---

## 📁 Project Structure

Task1/
- ├── api/
- │ ├── app.py # Flask API
- │ ├── model.pkl # Trained ML model
- ├── streamlit_app.py # Streamlit UI
- ├── requirements.txt # Dependencies
- ├── Dockerfile # For Flask API container
- ├── docker-compose.yml # Multi-service config
- ├── Model/
- │ ├── model.ipynp # ML model
- └── README.md


## ▶️ Running Locally (without Docker)

```bash
# Clone the project
git clone https://github.com/202202070/Iris-Classifier

# Change Directory
cd flask_api_python/api

# Install the requirements
pip3 install -r requirements.txt

# Run the script in Python
python3 app.py

```
## ▶️ Running with Docker (Manual)

```bash
# Build the Docker image
docker build -t flask_api -f Dockerfile .

# Run the Docker container
docker run -p 8501:8501 -p 5000:5000 flask_api

```
## ▶️ Running the Streamlit App
```
# Run the Streamlit app
streamlit run streamlit_app.py

```
## ▶️ Testing the API with Postman

```bash
# 1. Open Postman
# 2. Set method to POST
# 3. Use this URL:
http://localhost:5000/predict

# 4. Go to the "Body" tab → select "raw" → choose "JSON" format
# 5. Paste the following sample input:
{
  "feature_array":[4.9, 2.9, 1.2, 0.3]
}

# 6. Click "Send"

# ✅ Expected Response:
{
  "prediction": [0]
}

