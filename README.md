# 🧠 Diabetes Risk Prediction – Deep Learning Model

### Healthcare AI | Neural Networks | TensorFlow | Clinical ML Evaluation

---

## 📌 Overview

This repository contains a Deep Learning model developed to predict diabetes risk using structured clinical data.

The objective was to evaluate whether a neural network architecture could outperform classical machine learning models on a small, structured healthcare dataset.

The model was implemented using **TensorFlow/Keras** and evaluated using clinically relevant metrics, with particular emphasis on **Recall (Sensitivity)**.

---

## 🎯 Clinical Motivation

In medical screening systems:

* False Negative = Missed diagnosis
* Missed diagnosis = Delayed treatment and complications

Therefore, Recall was prioritized over Accuracy during model evaluation.

This project explores the performance trade-offs between Deep Learning and classical Machine Learning in small structured clinical datasets.

---

## 📊 Dataset

* 768 observations
* 8 numerical clinical features
* Binary outcome (0 = Non-diabetic, 1 = Diabetic)
* Moderate class imbalance (~65% / 35%)

Features include:

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age

Biologically implausible zero values were treated as missing and imputed using median imputation.

---

## ⚙️ Model Architecture

The neural network architecture consisted of:

* Input Layer (8 features)
* Dense Layer (ReLU activation)
* Dropout Layer
* Dense Layer (ReLU activation)
* Dropout Layer
* Output Layer (Sigmoid activation)

Regularization techniques applied:

* Dropout
* L2 regularization
* Early stopping
* Class weighting

Optimizer: Adam
Loss Function: Binary Crossentropy

---

## 📈 Model Performance

Test Results:

* **Recall:** 0.075
* **ROC-AUC:** 0.53

---

## 🔎 Interpretation of Results

The Deep Learning model significantly underperformed compared to the XGBoost model developed in the parallel ML pipeline.

Key reasons:

1. Small dataset size (n = 768)
2. Structured tabular data (DL performs better on large unstructured datasets)
3. Limited feature complexity
4. Insufficient data volume to fully optimize neural network parameters

This project reinforces an important insight:

> Deep Learning is not universally superior — model selection must match data structure and scale.

---

## 🏗 Training Pipeline

1. Data cleaning and zero-value correction
2. Median imputation
3. Feature scaling (StandardScaler)
4. Stratified train/test split
5. Class-weighted training
6. Early stopping to prevent overfitting

---

## 📂 Repository Structure

```
├── dl_model.ipynb
├── deep_learning_model.h5
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Scikit-Learn

---

## ⚖️ Responsible AI Considerations

* Model intended for educational and research purposes only
* Not validated for clinical deployment
* Requires external validation before real-world use
* Performance limitations highlight importance of proper model selection

---

## 💡 Key Takeaways

* Deep learning requires sufficient data volume to generalize effectively.
* Classical ML models often outperform neural networks on small structured clinical datasets.
* Metric selection (Recall vs Accuracy) fundamentally changes model evaluation in healthcare AI.

---

## 👨‍⚕️ Author

**Ntimi Mwambasi**

Medical Doctor | Healthcare AI/ML | Clinical Decision Support Systems
