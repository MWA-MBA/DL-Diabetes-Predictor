# Quick Start Guide

Get the Diabetes Prediction Service running in minutes!

## 🚀 Quick Start (5 minutes)

### Prerequisites
- Python 3.11+
- Docker (optional)
- Git

### Option 1: Run Locally (Recommended for Development)

```bash
# 1. Navigate to project directory
cd "c:\Users\windows 10\Desktop\DL Diabetes Predictor"

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # On Mac/Linux: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4a. Run Streamlit UI (Interactive Dashboard)
streamlit run dl_app.py
# Opens at: http://localhost:8501

# 4b. OR Run FastAPI Backend (API Server)
uvicorn api:app --reload
# API Docs at: http://localhost:8000/docs
```

### Option 2: Run with Docker Compose (Recommended for Production)

```bash
# 1. Install Docker Desktop (if not already installed)

# 2. Navigate to project directory
cd "c:\Users\windows 10\Desktop\DL Diabetes Predictor"

# 3. Build and start services
docker-compose up --build

# Access:
# Streamlit: http://localhost:8501
# FastAPI: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

---

## 📋 What Each Component Does

### Streamlit App (`dl_app.py`)
- Interactive web interface
- Easy-to-use sliders for patient inputs
- Real-time predictions
- Beautiful visualization
- **Port**: 8501

### FastAPI Backend (`api.py`)
- RESTful API endpoints
- Swagger/OpenAPI documentation
- Batch predictions
- Health checks
- Production-ready
- **Port**: 8000

### Deep Learning Model (`deep_learning_model.keras`)
- Pre-trained TensorFlow model
- Uses 8 patient health metrics
- Binary classification (Diabetes: Yes/No)
- ~35KB file size

---

## 🧪 Quick Test

### Test via Browser (UI)
1. Open `http://localhost:8501`
2. Adjust sliders for patient data
3. Click "Predict"
4. View results

### Test via API (Terminal)

```bash
# Single prediction
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

### Test via Python

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "pregnancies": 3,
    "glucose": 117,
    "blood_pressure": 72,
    "skin_thickness": 29,
    "insulin": 125,
    "bmi": 32.3,
    "diabetes_pedigree_function": 0.3725,
    "age": 29
}

response = requests.post(url, json=data)
print(response.json())
# Output: {"prediction": 0, "probability": 0.35, "confidence": "Medium"}
```

---

## 📚 API Documentation

Once running, view interactive docs:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🔧 Common Commands

```bash
# Check if services are running
docker ps  # Docker containers
lsof -i :8501  # Streamlit port
lsof -i :8000  # API port

# Stop services
docker-compose down

# View logs
docker-compose logs -f api
docker-compose logs -f web

# Rebuild images
docker-compose build --no-cache

# Run single service
docker-compose up api      # Only FastAPI
docker-compose up web      # Only Streamlit
```

---

## ❌ Troubleshooting

### "Model file not found"
- Ensure `deep_learning_model.keras` is in project root
- Check file permissions

### "Port already in use"
```bash
# Kill process using port
lsof -ti:8501 | xargs kill -9  # Streamlit
lsof -ti:8000 | xargs kill -9  # FastAPI
```

### "Module not found" errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Docker issues
```bash
# Remove old containers/images
docker system prune -a

# Rebuild everything
docker-compose up --build --force-recreate
```

---

## 📖 Next Steps

1. ✅ **Run the application** using one of the options above
2. 📖 **Read** [README.md](README.md) for detailed documentation
3. 🚀 **Deploy** to Render using [GITHUB_SETUP.md](GITHUB_SETUP.md)
4. 🧪 **Test** the endpoints with the examples above
5. 📝 **Customize** for your needs

---

## 📞 Need Help?

- Check [README.md](README.md) for complete documentation
- Review error messages carefully
- Check Docker/Python logs for details
- See [GITHUB_SETUP.md](GITHUB_SETUP.md) for deployment help

---

**Ready to go! Pick an option above and run it now.** 🎉
