# Maternal Health Risk Prediction AI Agent

This project is an AI-powered web application designed to predict maternal health risks during pregnancy. It leverages machine learning techniques to assess risks based on key health parameters, offering a modern and user-friendly interface for users to interact with.

## Project Purpose
Pregnancy is a critical period for both the mother and the child. This project aims to provide a reliable tool for predicting health risks during pregnancy to assist healthcare providers and expectant mothers in taking timely preventative measures. By utilizing a dataset aligned with Bosnian and European health standards, the application delivers localized and accurate insights.

## Key Features
- **Risk Prediction**: Predict the maternal health risk level based on parameters such as:
    - Age
    - Systolic and diastolic blood pressure
    - Glucose concentration
    - Body temperature 
    - Heart rate
- **Model Retraining**: Add new data directly through the interface to enhance the prediction model's accuracy over time.
- **Modern Web Interface**: A user-friendly interface designed with accessibility and simplicity in mind.
- **Machine Learning Backend**: Powered by a Random Forest Classifier for robust and accurate predictions.

## Technologies Used
- **Frontend:**
    - HTML
    - CSS
    - JavaScript
- **Backend:**
    - Python (Flask framework)
    - Pre-trained Random Forest Classifier
- **Dataset:**
    - Maternal health data from the UCI Machine Learning Repository, adapted to regional standards.

## Project Structure
- **backend/:**
    - **app.py**: The Flask application.
    - **model.pkl**: The serialized machine learning model.
    - **utils.py**: Utility functions for data processing and model operations.
- **dataset:**
    - The **.csv file** containing maternal health data.
- **frontend/:**
    - **index-html**: The web application interface.
    - **script.js**: JavaScript for dynamic functionality.
    - **styles.css**: Custom styles for the application.

## Installation guide
In **requirements.txt** file