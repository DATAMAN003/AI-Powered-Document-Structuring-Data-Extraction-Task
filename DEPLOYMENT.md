# Deployment Guide

## Quick Start (Local Development)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Run Command-Line Extraction**
```bash
python extract_data_enhanced.py
```

3. **Run Web Application**
```bash
python app.py
```

Then open your browser to: `http://localhost:5000`

---

## Cloud Deployment Options

### Option 1: Heroku (Recommended for Demo)

1. **Install Heroku CLI**
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

2. **Create Procfile**
```
web: gunicorn app:app
```

3. **Add gunicorn to requirements.txt**
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

4. **Deploy**
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

### Option 2: Railway.app

1. **Connect GitHub Repository**
   - Go to railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"

2. **Configure**
   - Railway auto-detects Python
   - Set start command: `python app.py`
   - Deploy automatically

### Option 3: Render.com

1. **Create New Web Service**
   - Connect your GitHub repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

2. **Configure Environment**
   - Python 3.11
   - Auto-deploy on push

### Option 4: PythonAnywhere

1. **Upload Files**
```bash
# Upload via web interface or git clone
```

2. **Create Virtual Environment**
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

3. **Configure WSGI**
```python
import sys
path = '/home/yourusername/your-project'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### Option 5: AWS EC2

1. **Launch EC2 Instance**
   - Ubuntu 22.04 LTS
   - t2.micro (free tier)

2. **Install Dependencies**
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

3. **Setup Application**
```bash
git clone your-repo
cd your-repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

4. **Configure Nginx**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

5. **Run with Gunicorn**
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

---

## Environment Variables

For production deployment, set these environment variables:

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here
export MAX_CONTENT_LENGTH=16777216  # 16MB
```

---

## Testing the Deployment

1. **Health Check**
```bash
curl http://your-domain.com/
```

2. **Upload Test**
```bash
curl -X POST -F "file=@Data Input.pdf" http://your-domain.com/upload
```

3. **Demo Page**
```bash
curl http://your-domain.com/demo
```

---

## Troubleshooting

### Issue: Module not found
**Solution**: Ensure all dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
**Solution**: Change port in app.py or kill existing process
```bash
# Change port
app.run(port=8000)

# Or kill process
lsof -ti:5000 | xargs kill -9
```

### Issue: PDF extraction fails
**Solution**: Ensure PDF is not encrypted or image-based
```bash
# Check PDF
pdfinfo "Data Input.pdf"
```

---

## Performance Optimization

1. **Enable Caching**
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

2. **Use Production Server**
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

3. **Add Rate Limiting**
```python
from flask_limiter import Limiter
limiter = Limiter(app, default_limits=["100 per hour"])
```

---

## Security Considerations

1. **File Upload Validation**
   - Already implemented: PDF only, 16MB max
   - Consider adding virus scanning

2. **HTTPS**
   - Use Let's Encrypt for free SSL
   - Configure in Nginx/Apache

3. **Input Sanitization**
   - Already using secure_filename()
   - Temporary file cleanup implemented

---

## Monitoring

### Application Logs
```bash
# View logs
tail -f app.log

# Or use cloud provider logs
heroku logs --tail
```

### Performance Metrics
```python
# Add to app.py
import time
from functools import wraps

def timing_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"{f.__name__} took {end-start:.2f}s")
        return result
    return wrapper
```

---

## Scaling

### Horizontal Scaling
- Use load balancer (AWS ELB, Nginx)
- Deploy multiple instances
- Share session storage (Redis)

### Vertical Scaling
- Increase instance size
- Add more workers to Gunicorn
- Optimize extraction algorithms

---

## Backup & Recovery

1. **Database Backup** (if using database)
```bash
# Automated daily backups
0 2 * * * pg_dump mydb > backup_$(date +\%Y\%m\%d).sql
```

2. **File Storage**
   - Use S3 for uploaded files
   - Implement retention policy

---

## Support

For deployment issues:
1. Check application logs
2. Verify all dependencies installed
3. Test with sample PDF first
4. Contact: [your-email]

---

## License

This project is for educational/assignment purposes.
