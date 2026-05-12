# Disease Prediction System (Healthcare Analytics)



The **Disease Prediction System** is a Machine Learning-based web application that predicts the likelihood of a disease (Heart Disease) using patient medical data.
It helps in early diagnosis and supports doctors in making better healthcare decisions.

---

##  Objectives

* Predict disease based on patient health parameters
* Assist doctors in early diagnosis
* Reduce manual analysis and errors
* Improve healthcare decision-making

---

## Problem Statement

Traditional healthcare systems rely heavily on manual diagnosis, which:

* Takes more time
* Depends on doctor experience
* Makes early detection difficult

This project automates disease prediction using Machine Learning.

---

## Proposed Solution

The system:

1. Takes patient input (Age, Blood Pressure, Cholesterol, Sugar Level)
2. Applies a trained Machine Learning model
3. Predicts whether the patient has a disease or not

---

## Technologies Used

* **Programming Language:** Python
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
  * Matplotlib
  * Seaborn
* **Framework:** Flask
* **Tools:** VS Code, Jupyter Notebook

---

## Machine Learning Model

* Algorithm: Random Forest Classifier
* Type: Classification
* Evaluation Metric: Accuracy Score

---

## 📁 Project Structure

```
Disease-Prediction-System/
│
├── app.py
├── train_model.py
├── model.pkl
├── accuracy.txt
├── dataset.csv
│
└── templates/
    └── index.html
```

---

##  How to Run the Project

### Step 1: Install dependencies

```
pip install pandas numpy scikit-learn flask matplotlib seaborn
```

### Step 2: Train the model

```
python train_model.py
```

### Step 3: Run the Flask app

```
python app.py
```

### Step 4: Open in browser

```
http://127.0.0.1:5000
```

---

##  Output

* User enters medical details
* System predicts:

  * 💚 No Disease
  * ❤️ Disease Detected
* Displays model accuracy

---

##  Features

* Simple and user-friendly interface
* Real-time disease prediction
* Accuracy display
* Data visualization using graphs

---

##  Advantages

* Early disease detection
* Fast and accurate predictions
* Reduces human error
* Supports medical professionals

---

## Limitations

* Depends on dataset quality
* Limited to trained data
* Cannot replace doctors

---

##  Future Enhancements

* Add more diseases
* Use Deep Learning models
* Integrate with wearable devices
* Deploy as mobile/web application

---

## Conclusion

This project demonstrates how Machine Learning can be used in healthcare to predict diseases efficiently and improve decision-making processes.

---

##  Author

* Poornima M

---
