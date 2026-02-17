🎬 Movie Recommendation System

This project is an intelligent movie recommendation system that suggests movies to users based on their preferences and viewing history. The system uses Collaborative Filtering and Content-Based Filtering techniques and is deployed with an interactive Streamlit GUI.

📌 Features

Personalized movie recommendations

Collaborative Filtering & Content-Based algorithms

Interactive web interface using Streamlit

Pre-trained similarity model with ~80% accuracy

End-to-end machine learning pipeline

🛠️ Technologies Used

Programming Language: Python

Libraries: NumPy, Pandas, Matplotlib, Scikit-learn

Frameworks: Flask, Streamlit

Machine Learning: Linear Regression, Polynomial Regression

Model Storage: Pickle (.pkl files)

📂 Project Structure
📦 Movie-Recommendation-System
 ├── data/
 ├── app.py
 ├── requirements.txt
 ├── similarity.pkl
 ├── movie_list.pkl
 └── README.md

⚙️ Installation & Setup
Step 1: Clone or Download the Project

Download the repository and unzip all files into a single directory.

git clone <repository-url>
cd Movie-Recommendation-System

Step 2: Generate Model Files

Run the data preprocessing and model generation scripts.

After execution, the following files will be created:

similarity.pkl – Stores similarity scores between movies

movie_list.pkl – Contains the processed movie dataset

These files are required for the recommendation engine.

Step 3: Install Dependencies

Install all required Python libraries using:

pip install -r requirements.txt

Step 4: Run the Application

Start the Streamlit application using:

streamlit run app.py


A local host URL will be generated

Open the URL in your browser to access the application

🎯 How It Works

User selects a movie from the list

The system computes similarity using the pre-trained model

Top recommended movies are displayed instantly

Results are shown through a clean and interactive GUI

📊 Model Details

Uses Collaborative Filtering and Content-Based Filtering

Similarity model (similarity.pkl) achieves approximately 80% accuracy

Built using Scikit-learn and Python data science libraries

📸 Screenshots (Optional)

Add screenshots of the Streamlit UI here

📷 Home Page  
📷 Movie Selection  
📷 Recommendation Output

🚀 Future Enhancements

User login & profile-based recommendations

Real-time movie database integration

Deep learning–based recommendation models

Deployment on cloud platforms (AWS / GCP / Azure)
