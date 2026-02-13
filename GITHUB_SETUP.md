# GitHub Setup Guide

Follow these steps to push your project to GitHub:

## Step 1: Create a Repository on GitHub

1. Go to [GitHub.com](https://github.com)
2. Click the **+** icon in the top-right corner
3. Select **New repository**
4. Fill in the details:
   - **Repository name**: `DL-Diabetes-Predictor`
   - **Description**: `Deep Learning ML service for diabetes prediction with Streamlit UI and FastAPI backend`
   - **Visibility**: Choose **Public** (or Private if preferred)
   - **Do NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **Create repository**

## Step 2: Add Remote and Push to GitHub

After the repository is created, you'll see commands on GitHub. Run these locally:

```bash
cd "c:\Users\windows 10\Desktop\DL Diabetes Predictor"

# Add the remote repository
git remote add origin https://github.com/YOUR_USERNAME/DL-Diabetes-Predictor.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username.**

## Step 3: Verify on GitHub

1. Refresh your GitHub repository page
2. You should see all your files uploaded
3. Verify the folder structure is correct

## Step 4: (Optional) Add Collaborators

1. Go to your repository settings
2. Click **Access** → **Collaborators**
3. Click **Add people** and enter GitHub usernames

## Step 5: Set Up Deployment on Render

### Option A: Automatic Deployment via Render.yaml

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **+ New** → **Web Service**
3. Select **Build and deploy from a Git repository**
4. Connect your GitHub account
5. Select your `DL-Diabetes-Predictor` repository
6. Render will auto-detect `render.yaml` configuration

### Option B: Manual Configuration

1. **Deploy FastAPI Service:**
   - Name: `diabetes-prediction-api`
   - Environment: Python 3.11
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
   - Add environment variable `ENVIRONMENT=production`

2. **Deploy Streamlit Service:**
   - Name: `diabetes-prediction-web`
   - Environment: Python 3.11
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run dl_app.py --server.port=8501 --server.address=0.0.0.0 --client.toolbarMode=minimal`

## Testing Your Deployment

Once deployed on Render:

1. **API Endpoint**: `https://<your-api-service>.onrender.com`
   - API Docs: `https://<your-api-service>.onrender.com/docs`
   - Health Check: `https://<your-api-service>.onrender.com/health`

2. **Web Interface**: `https://<your-web-service>.onrender.com`

## Troubleshooting

### Issue: "Repository not found"
- Check spelling of GitHub username
- Verify you've created the repository on GitHub
- Check authentication (run `git remote -v` to see current remotes)

### Issue: "Permission denied (publickey)"
- Go to Settings on GitHub → Developer settings → Personal access tokens
- Create a new token with `repo` scope
- Use the token instead of password when prompted

### Issue: Push fails with "fatal: refusing to merge unrelated histories"
```bash
git fetch origin
git merge origin/main --allow-unrelated-histories
git push origin main
```

### Issue: Model file too large
If `deep_learning_model.keras` is > 100MB:
1. Use Git LFS (Large File Storage):
   ```bash
   git lfs install
   git lfs track "*.keras"
   git add .gitattributes
   git add deep_learning_model.keras
   git commit -m "Add model file with LFS"
   git push origin main
   ```
2. Or upload the model separately to cloud storage and download during deployment

## Useful Git Commands

```bash
# Check git status
git status

# View commit history
git log --oneline

# Create a new branch
git checkout -b feature/new-feature

# Switch branches
git checkout main

# Push changes
git push origin main

# Pull latest changes
git pull origin main
```

## Next Steps

- Set up CI/CD pipeline (GitHub Actions)
- Configure automatic tests
- Add deployment badges to README
- Set up monitoring and logging
