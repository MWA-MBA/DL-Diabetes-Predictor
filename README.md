# Diabetes Prediction ML Service

A comprehensive machine learning project implementing a deep learning model for diabetes prediction with both a user-friendly Streamlit interface and a production-ready FastAPI backend.

## 🚀 Features

- **Streamlit Web Interface** - Interactive UI for single patient predictions
- **FastAPI REST API** - High-performance endpoints with automatic Swagger documentation
- **Deep Learning Model** - TensorFlow/Keras neural network for accurate predictions
- **Dockerized** - Easy deployment with Docker and Docker Compose
- **Cloud Ready** - Pre-configured for deployment on Render
- **Batch Processing** - Support for multiple patient predictions via API

## 📋 Project Structure

```
.
├── api.py                          # FastAPI application
├── dl_app.py                       # Streamlit web interface
├── deep_learning_model.keras       # Pre-trained model
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container configuration
├── docker-compose.yml              # Multi-container orchestration
├── render.yaml                     # Render deployment config
├── .gitignore                      # Git ignore rules
├── .dockerignore                   # Docker ignore rules
├── .env.example                    # Environment variables template
├── Notebook/                       # Jupyter notebooks
│   └── Diabetes_ML+DL_Prediction_Colab Notebook.ipynb
└── README.md                       # This file
```

## 📊 Model Details

The model predicts diabetes risk based on 8 health metrics:
- **Pregnancies**: Number of times pregnant (0-17)
- **Glucose**: Plasma glucose concentration (44-199 mg/dL)
- **Blood Pressure**: Diastolic blood pressure (24-122 mmHg)
- **Skin Thickness**: Triceps skin fold thickness (7-99 mm)
- **Insulin**: 2-hour serum insulin (14-846 µU/ml)
- **BMI**: Body mass index (18.2-67.1 kg/m²)
- **Diabetes Pedigree Function**: Genetic predisposition (0.078-2.42)
- **Age**: Age in years (21-81)

**Output**: Binary classification (0 = No diabetes, 1 = Diabetes)

## 🔧 Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DL-Diabetes-Predictor
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the model file exists**
   ```bash
   # Place deep_learning_model.keras in the root directory
   ```

## 🏃 Running the Application

### Option 1: Streamlit Interface (Local)
```bash
streamlit run dl_app.py
```
Open browser to `http://localhost:8501`

### Option 2: FastAPI Backend (Local)
```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```
- API docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Option 3: Both Services with Docker Compose
```bash
docker-compose up --build
```
- Streamlit: `http://localhost:8501`
- FastAPI: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

## 🐳 Docker

### Build Docker Image
```bash
docker build -t diabetes-predictor .
```

### Run Container
```bash
# FastAPI only
docker run -p 8000:8000 diabetes-predictor

# Or with Streamlit
docker run -p 8501:8501 diabetes-predictor streamlit run dl_app.py --server.port=8501 --server.address=0.0.0.0
```

## 📡 API Endpoints

### Health Check
```bash
GET /health
```

### Single Prediction
```bash
POST /predict
Content-Type: application/json

{
  "pregnancies": 3,
  "glucose": 117,
  "blood_pressure": 72,
  "skin_thickness": 29,
  "insulin": 125,
  "bmi": 32.3,
  "diabetes_pedigree_function": 0.3725,
  "age": 29
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.35,
  "confidence": "Medium"
}
```

### Batch Prediction
```bash
POST /predict-batch
Content-Type: application/json

[
  {
    "pregnancies": 3,
    "glucose": 117,
    ...
  },
  {
    "pregnancies": 2,
    "glucose": 105,
    ...
  }
]
```

### Model Information
```bash
GET /model-info
```

## 🚀 Deployment on Render

### Automatic Deployment

1. **Push to GitHub**
   ```bash
   git push origin main
   ```

2. **Connect to Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Connect your GitHub repository
   - Create new Web Service
   - Use `render.yaml` for configuration

### Manual Deployment

1. Create a new Web Service on Render
2. Select your GitHub repository
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn api:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3.11
4. Deploy

## 📚 API Documentation

Once the API is running, view interactive documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🧪 Testing

### Test the API with curl
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 3,
    "glucose": 117,
    "blood_pressure": 72,
    "skin_thickness": 29,
    "insulin": 125,
    "bmi": 32.3,
    "diabetes_pedigree_function": 0.3725,
    "age": 29
  }'
```

### Test with Python
```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={
        "pregnancies": 3,
        "glucose": 117,
        "blood_pressure": 72,
        "skin_thickness": 29,
        "insulin": 125,
        "bmi": 32.3,
        "diabetes_pedigree_function": 0.3725,
        "age": 29
    }
)
print(response.json())
```

## 🔐 Environment Variables

Create a `.env` file (based on `.env.example`):

```env
ENVIRONMENT=development
PORT=8000
DEBUG=true
```

## 📝 Requirements

See [requirements.txt](requirements.txt) for all dependencies:
- Python 3.11+
- TensorFlow 2.13+
- Streamlit 1.28+
- FastAPI 0.104+
- Uvicorn 0.24+
- Pandas 2.0+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 📞 Support

For issues and questions:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Include error logs and environment details

## 🎯 Roadmap

- [ ] Add model retraining pipeline
- [ ] Implement user authentication
- [ ] Add database for prediction history
- [ ] Create mobile app
- [ ] Add more visualization features
- [ ] Implement model versioning
- [ ] Add unit and integration tests
- [ ] Create CI/CD pipeline

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Render Documentation](https://render.com/docs)

---

**Last Updated**: February 2026  
**Version**: 1.0.0
