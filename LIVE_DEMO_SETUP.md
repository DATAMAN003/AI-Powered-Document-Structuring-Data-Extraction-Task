# 🌐 Live Demo Setup Guide

Get your demo online in **5 minutes** with a free temporary domain!

---

## 🚀 **Option 1: Railway.app** (EASIEST - Recommended!)

**✅ Pros**: Free, automatic HTTPS, no credit card, 2-minute setup  
**⏱️ Time**: 2-5 minutes  
**💰 Cost**: FREE (500 hours/month)

### Step-by-Step:

1. **Go to Railway.app**
   - Visit: https://railway.app
   - Click "Start a New Project"
   - Sign in with GitHub

2. **Deploy from GitHub**
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Railway auto-detects Python and deploys!

3. **Get Your URL**
   - Click "Settings" → "Generate Domain"
   - Your demo will be at: `https://your-app.up.railway.app`

**That's it!** ✅ Your demo is live!

---

## 🎯 **Option 2: Render.com** (Also Very Easy!)

**✅ Pros**: Free, automatic HTTPS, simple setup  
**⏱️ Time**: 3-5 minutes  
**💰 Cost**: FREE

### Step-by-Step:

1. **Go to Render.com**
   - Visit: https://render.com
   - Sign up with GitHub

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repo

3. **Configure**
   - Name: `ai-document-extraction`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Click "Create Web Service"

4. **Get Your URL**
   - Your demo: `https://ai-document-extraction.onrender.com`

**Done!** ✅

---

## ⚡ **Option 3: Vercel** (Fastest!)

**✅ Pros**: Instant deployment, free, automatic HTTPS  
**⏱️ Time**: 1-2 minutes  
**💰 Cost**: FREE

### Step-by-Step:

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Deploy**
```bash
cd C:\Users\TOSIN\Desktop\HMWK3
vercel
```

3. **Follow Prompts**
   - Login with GitHub
   - Confirm project settings
   - Deploy!

4. **Get URL**
   - Your demo: `https://your-project.vercel.app`

**Live in 60 seconds!** ✅

---

## 🔥 **Option 4: Heroku** (Most Popular)

**✅ Pros**: Industry standard, reliable  
**⏱️ Time**: 5-10 minutes  
**💰 Cost**: FREE (with credit card verification)

### Step-by-Step:

1. **Install Heroku CLI**
   - Download: https://devcenter.heroku.com/articles/heroku-cli
   - Install and restart terminal

2. **Login**
```bash
heroku login
```

3. **Create App**
```bash
cd C:\Users\TOSIN\Desktop\HMWK3
heroku create ai-doc-extraction-demo
```

4. **Deploy**
```bash
git init
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

5. **Open**
```bash
heroku open
```

**Your URL**: `https://ai-doc-extraction-demo.herokuapp.com`

---

## 🎨 **Option 5: Replit** (No Installation Needed!)

**✅ Pros**: Browser-based, no installation, instant  
**⏱️ Time**: 2-3 minutes  
**💰 Cost**: FREE

### Step-by-Step:

1. **Go to Replit**
   - Visit: https://replit.com
   - Sign up (free)

2. **Create New Repl**
   - Click "+ Create Repl"
   - Choose "Python"
   - Name: "AI Document Extraction"

3. **Upload Files**
   - Drag and drop all your files
   - Or use "Upload folder"

4. **Run**
   - Click "Run" button
   - Replit automatically installs dependencies
   - Your demo is live!

5. **Get URL**
   - Your demo: `https://ai-document-extraction.username.repl.co`

**Instant demo!** ✅

---

## 🌟 **Option 6: PythonAnywhere** (Python-Specific)

**✅ Pros**: Python-focused, free tier  
**⏱️ Time**: 10-15 minutes  
**💰 Cost**: FREE

### Step-by-Step:

1. **Sign Up**
   - Visit: https://www.pythonanywhere.com
   - Create free account

2. **Upload Files**
   - Go to "Files" tab
   - Upload your project files

3. **Create Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Python version: 3.10

4. **Configure WSGI**
   - Edit WSGI configuration file:
```python
import sys
path = '/home/yourusername/ai-document-extraction'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

5. **Reload**
   - Click "Reload" button
   - Your demo: `https://yourusername.pythonanywhere.com`

---

## 📊 **Comparison Table**

| Platform | Setup Time | Difficulty | Free Tier | Custom Domain | HTTPS |
|----------|------------|------------|-----------|---------------|-------|
| **Railway** | 2 min | ⭐ Easy | ✅ Yes | ✅ Yes | ✅ Auto |
| **Render** | 3 min | ⭐ Easy | ✅ Yes | ✅ Yes | ✅ Auto |
| **Vercel** | 1 min | ⭐ Easy | ✅ Yes | ✅ Yes | ✅ Auto |
| **Heroku** | 5 min | ⭐⭐ Medium | ✅ Yes* | ✅ Yes | ✅ Auto |
| **Replit** | 2 min | ⭐ Easy | ✅ Yes | ❌ No | ✅ Auto |
| **PythonAnywhere** | 10 min | ⭐⭐ Medium | ✅ Yes | ❌ No | ✅ Auto |

*Heroku requires credit card verification

---

## 🎯 **My Recommendation**

### For Fastest Setup (1-2 minutes):
**Use Railway.app** - Just connect GitHub and click deploy!

### For No Installation:
**Use Replit** - Everything in browser

### For Most Professional:
**Use Render.com** - Great free tier, professional URLs

---

## 🚀 **Quick Start: Railway (Recommended)**

Since I've already created the necessary files (`Procfile`, `railway.json`), here's what you do:

### 1. Push to GitHub First

```bash
cd C:\Users\TOSIN\Desktop\HMWK3

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "AI Document Extraction - Ready for deployment"

# Create GitHub repo and push
# (Follow GITHUB_SETUP.md)
```

### 2. Deploy to Railway

1. Go to https://railway.app
2. Click "Start a New Project"
3. Choose "Deploy from GitHub repo"
4. Select your repository
5. Click "Deploy"
6. Wait 2-3 minutes
7. Click "Settings" → "Generate Domain"

**Done!** Your demo is live at: `https://your-app.up.railway.app`

---

## 🔧 **Files Already Created for You**

I've created these deployment files:

✅ `Procfile` - Tells platforms how to run your app  
✅ `railway.json` - Railway configuration  
✅ `requirements.txt` - Updated with gunicorn  

You're ready to deploy immediately!

---

## 🎬 **Demo Features**

Your live demo will have:
- ✅ Upload interface (drag-and-drop)
- ✅ Real-time processing
- ✅ Download Excel results
- ✅ Demo page with sample data
- ✅ Professional UI
- ✅ Mobile responsive

---

## 🐛 **Troubleshooting**

### Issue: "Application Error"
**Solution**: Check logs in platform dashboard

### Issue: "Module not found"
**Solution**: Ensure `requirements.txt` is complete
```bash
pip freeze > requirements.txt
```

### Issue: "Port binding error"
**Solution**: Update app.py to use PORT environment variable
```python
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

---

## 📞 **Need Help?**

### Railway Support
- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway

### Render Support
- Docs: https://render.com/docs
- Community: https://community.render.com

### Heroku Support
- Docs: https://devcenter.heroku.com
- Help: https://help.heroku.com

---

## ✨ **Pro Tips**

1. **Use Railway for quickest setup** - 2 minutes total
2. **Add environment variables** in platform settings if needed
3. **Monitor logs** to debug issues
4. **Share the URL** in your assignment submission
5. **Keep it running** - most free tiers have enough hours

---

## 🎉 **You're Ready!**

Choose your platform and deploy in minutes. Railway is the fastest!

**Next Steps**:
1. Push code to GitHub (if not done)
2. Go to Railway.app
3. Deploy from GitHub
4. Get your live demo URL
5. Share in assignment submission

**Good luck! 🚀**
