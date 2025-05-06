"# Gemstone_price_prediction" 
# Gemstone Price Prediction

A machine‐learning pipeline to predict the market price of polished gemstones based on their physical and optical properties.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Installation](#installation)  


---

## Project Overview

This project builds and compares regression models (Linear Regression, Random Forest, XGBoost) to estimate the selling price of gemstones given features like carat weight, cut, color, clarity, and dimensions.

---

## Features

- **Data Cleaning & EDA**  
- **Feature Engineering** (log-transform, derived volume, encoding)  
- **Model Training & Evaluation** with cross-validation  
- **Hyperparameter Tuning** via GridSearchCV  
- **Flask API** for real-time price prediction  

---

## Tech Stack

- Python  
- pandas, NumPy, matplotlib  
- scikit-learn, XGBoost  
- Flask  
- Jupyter Notebook  

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/kuldeepkd0603/Gemstone_price_prediction.git
   cd gemstone-price-prediction
2. **Install requirement.txt file**
   ```bash
    pip install -r requirements.txt 

3. **Open two different-different for run app and api seprately**
   ```base 
   python api.py
4.**on other terminal run api**
   ```base
   cd app
   python app.py


