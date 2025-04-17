# 🎓 Student Performance Predictor

A smart web app that predicts whether a student will **Pass** or **Fail** based on academic and lifestyle factors using **Machine Learning**. Built with **Python, Scikit-learn**, and **Streamlit**.

---

## 🚀 Features

- ✅ Predicts student performance based on input factors
- 🧠 ML-powered backend (Logistic Regression)
- 🎯 Real-time predictions through Streamlit UI
- 📋 Simple and clean interface
- 💡 Personalized advice based on prediction

---

## 📊 Dataset

The app uses the [Student Performance Dataset](https://www.kaggle.com/spscientist/students-performance-in-exams) from Kaggle.  
It includes:

- Study hours
- Sleep hours
- Internet usage
- Class attendance
- Past performance
- Parent's education level
- Extra-curricular activities

---

## 🧠 Machine Learning Model

- Algorithm: **Logistic Regression**
- Evaluation: Accuracy Score, Classification Report
- Serialization: `joblib`

---

## 📁 Project Structure
student-performance-predictor/ │ ├── app.py # Streamlit frontend app ├── model/ │ └── model.pkl # Trained ML model ├── data/ │ └── students.csv # Dataset (optional) ├── requirements.txt # Project dependencies └── README.md # Project documentation


---

## 🛠️ Setup Instructions

### ✅ Run Locally

1. **Clone the repository**
bash
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor
python -m venv env
# Activate the environment
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
pip install -r requirements.txt
streamlit run app.py

🌐 Deploy to Streamlit Cloud
Push your code and model.pkl to a public GitHub repo.

Go to Streamlit Cloud.

Click "New App", connect your GitHub, and select the repo.

Set app.py as the entry point.

Done! 🚀

🙋‍♂️ Author
Aditya
Full-stack & ML Developer
GitHub Profile :-https://github.com/ABaditya07

📄 License
Licensed under the MIT License. Feel free to use and modify.


🌟 If you found this helpful, give it a star on GitHub!


