"""
FastAPI application for Diabetes Prediction Model
Provides REST API endpoints with Swagger documentation
"""

import os
from typing import Optional
import numpy as np
import pandas as pd
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

# Load the trained DL model
try:
    model = tf.keras.models.load_model('deep_learning_model.keras')
except FileNotFoundError:
    raise RuntimeError("Model file 'deep_learning_model.keras' not found. Please ensure it's in the root directory.")

# Initialize FastAPI app
app = FastAPI(
    title="Diabetes Prediction API",
    description="Deep Learning API for predicting diabetes risk",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictionInput(BaseModel):
    """Input schema for diabetes prediction"""
    pregnancies: float = Field(..., ge=0, le=17, description="Number of pregnancies")
    glucose: float = Field(..., ge=44, le=199, description="Glucose level (mg/dL)")
    blood_pressure: float = Field(..., ge=24, le=122, description="Blood pressure (mmHg)")
    skin_thickness: float = Field(..., ge=7, le=99, description="Skin thickness (mm)")
    insulin: float = Field(..., ge=14, le=846, description="Insulin level (µU/ml)")
    bmi: float = Field(..., ge=18.2, le=67.1, description="Body Mass Index (kg/m²)")
    diabetes_pedigree_function: float = Field(..., ge=0.078, le=2.42, description="Diabetes pedigree function")
    age: float = Field(..., ge=21, le=81, description="Age (years)")

    class Config:
        json_schema_extra = {
            "example": {
                "pregnancies": 3,
                "glucose": 117,
                "blood_pressure": 72,
                "skin_thickness": 29,
                "insulin": 125,
                "bmi": 32.3,
                "diabetes_pedigree_function": 0.3725,
                "age": 29
            }
        }


class PredictionOutput(BaseModel):
    """Output schema for diabetes prediction"""
    prediction: int = Field(..., description="Prediction (0: No diabetes, 1: Diabetes)")
    probability: float = Field(..., description="Probability of diabetes (0-1)")
    confidence: str = Field(..., description="Confidence level of prediction")


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": True,
        "service": "Diabetes Prediction API"
    }


@app.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
async def predict_diabetes(input_data: PredictionInput):
    """
    Predict diabetes probability based on patient health metrics
    
    ### Input Parameters:
    - **pregnancies**: Number of pregnancies (0-17)
    - **glucose**: Glucose level in mg/dL (44-199)
    - **blood_pressure**: Blood pressure in mmHg (24-122)
    - **skin_thickness**: Skin thickness in mm (7-99)
    - **insulin**: Insulin level in µU/ml (14-846)
    - **bmi**: Body Mass Index in kg/m² (18.2-67.1)
    - **diabetes_pedigree_function**: Diabetes pedigree function (0.078-2.42)
    - **age**: Age in years (21-81)
    
    ### Returns:
    - **prediction**: 0 = No diabetes, 1 = Diabetes
    - **probability**: Probability score (0-1)
    - **confidence**: Confidence level (Low/Medium/High)
    """
    try:
        # Create DataFrame from input
        input_df = pd.DataFrame([{
            'Pregnancies': input_data.pregnancies,
            'Glucose': input_data.glucose,
            'BloodPressure': input_data.blood_pressure,
            'SkinThickness': input_data.skin_thickness,
            'Insulin': input_data.insulin,
            'BMI': input_data.bmi,
            'DiabetesPedigreeFunction': input_data.diabetes_pedigree_function,
            'Age': input_data.age
        }])

        # Make prediction
        prediction_proba = model.predict(input_df, verbose=0)[0][0]
        prediction = int(prediction_proba > 0.5)

        # Determine confidence level
        confidence_prob = max(prediction_proba, 1 - prediction_proba)
        if confidence_prob >= 0.8:
            confidence = "High"
        elif confidence_prob >= 0.6:
            confidence = "Medium"
        else:
            confidence = "Low"

        return PredictionOutput(
            prediction=prediction,
            probability=float(prediction_proba),
            confidence=confidence
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.post("/predict-batch", tags=["Prediction"])
async def predict_batch(patients: list[PredictionInput]):
    """
    Batch prediction for multiple patients
    
    ### Input:
    An array of patient records with the same fields as /predict endpoint
    
    ### Returns:
    An array of predictions with probabilities
    """
    try:
        if not patients:
            raise ValueError("Empty patient list")
        
        if len(patients) > 100:
            raise ValueError("Maximum 100 patients per request")

        # Create DataFrame from all patients
        data_list = []
        for patient in patients:
            data_list.append({
                'Pregnancies': patient.pregnancies,
                'Glucose': patient.glucose,
                'BloodPressure': patient.blood_pressure,
                'SkinThickness': patient.skin_thickness,
                'Insulin': patient.insulin,
                'BMI': patient.bmi,
                'DiabetesPedigreeFunction': patient.diabetes_pedigree_function,
                'Age': patient.age
            })

        input_df = pd.DataFrame(data_list)

        # Make predictions
        predictions_proba = model.predict(input_df, verbose=0).flatten()
        
        results = []
        for i, proba in enumerate(predictions_proba):
            prediction = int(proba > 0.5)
            confidence_prob = max(proba, 1 - proba)
            
            if confidence_prob >= 0.8:
                confidence = "High"
            elif confidence_prob >= 0.6:
                confidence = "Medium"
            else:
                confidence = "Low"

            results.append({
                "patient_id": i + 1,
                "prediction": prediction,
                "probability": float(proba),
                "confidence": confidence
            })

        return {
            "total_patients": len(patients),
            "predictions": results
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction error: {str(e)}")


@app.get("/model-info", tags=["Model"])
async def model_info():
    """Get information about the loaded model"""
    return {
        "model_name": "Deep Learning Diabetes Predictor",
        "input_features": [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age"
        ],
        "output": "Diabetes probability (0-1)",
        "framework": "TensorFlow/Keras",
        "threshold": 0.5
    }


if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("ENVIRONMENT", "development") == "development"
    )
