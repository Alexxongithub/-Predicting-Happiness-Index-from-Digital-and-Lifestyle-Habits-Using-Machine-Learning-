# -Predicting-Happiness-Index-from-Digital-and-Lifestyle-Habits-Using-Machine-Learning-
This project investigates how digital habits (e.g., screen time and social media usage) and lifestyle behaviors (e.g., sleep quality, exercise frequency, and stress levels) influence mental health and emotional balance.

We trained a Random Forest Regressor on a dataset containing behavioural and lifestyle features. The final model is deployed using FastAPI, and a simple, interactive HTML/CSS/JavaScript frontend allows users to input data and receive predictions in real time.

1. Objectives:

Build a predictive model using real-world lifestyle data.

Deploy the model to a web-accessible interface.

Allow users to input their daily habits and receive a predicted happiness score.

2. Motivation:

Excessive social media use and poor lifestyle habits are known to correlate with lower mental well-being. Providing predictive feedback empowers users to make informed behavioral adjustments.

3.Model Selection

Random Forest Regressor was chosen due to:

Ability to handle nonlinear relationships

Minimal preprocessing requirements

Implemented in Python using scikit-learn.

4. Running the System

Start the backend:

uvicorn main:app --reload


Open the frontend in a browser: http://127.0.0.1:8000

Input values and click Predict Happiness to get results.

