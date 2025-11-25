# 🚀 Simple Setup - One Script Does Everything!

## Super Easy - Just 3 Steps!

---

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 2: Configure API Key (Optional - for AI mode)

### Get FREE API Key:
1. Go to: https://console.groq.com
2. Sign up (free)
3. Create API key
4. Copy your key

### Add to .env file:
1. Open `.env` file in this folder
2. Replace the line:
   ```
   GROQ_API_KEY=
   ```
   With:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
3. Save the file

**Note**: If you skip this step, the system will use regex mode (which works great for the assignment!)

---

## Step 3: Run the Application

```bash
python run.py
```

That's it! 🎉

---

## What You'll See

```
======================================================================
🚀 Document Extraction System - Unified Runner
======================================================================

✅ Groq API key found - AI mode available!

======================================================================
What would you like to do?
======================================================================

1. Extract data from PDF (Regex - Fast, for assignment)
2. Extract data from PDF (AI - Intelligent, any document)
3. Run web application (Upload interface)
4. Exit

Enter your choice (1-4):
```

---

## Usage Options

### Option 1: Regex Extraction (Fast)
- Perfect for assignment
- Works with "Data Input.pdf"
- < 2 seconds processing
- No API key needed

### Option 2: AI Extraction (Intelligent)
- Works with ANY PDF
- Requires API key
- 10-60 seconds processing
- Auto-categorizes data

### Option 3: Web Application
- Upload interface
- Drag-and-drop
- Download results
- Demo mode

---

## Examples

### Extract Assignment PDF (Regex):
```
1. Run: python run.py
2. Choose: 1
3. Press Enter (uses Data Input.pdf)
4. Press Enter (saves to Output.xlsx)
5. Done! ✅
```

### Extract Any PDF (AI):
```
1. Run: python run.py
2. Choose: 2
3. Enter your PDF filename
4. Enter output filename
5. Done! ✅
```

### Run Web Interface:
```
1. Run: python run.py
2. Choose: 3
3. Open: http://localhost:5000
4. Upload and extract! ✅
```

---

## File Structure

```
.env                    - Your API key (don't commit!)
.env.example            - Example .env file
run.py                  - ONE script to run everything
extract_data_enhanced.py - Regex extraction
extract_data_ai.py      - AI extraction
app.py                  - Web application
```

---

## Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "API key not configured"
- Open `.env` file
- Add your Groq API key
- Or use Option 1 (regex mode - no API needed)

### "PDF not found"
- Make sure PDF is in the same folder
- Or provide full path: `C:\path\to\file.pdf`

---

## Quick Reference

| Command | What It Does |
|---------|--------------|
| `python run.py` | Start the application |
| Option 1 | Fast extraction (regex) |
| Option 2 | Smart extraction (AI) |
| Option 3 | Web interface |
| Option 4 | Exit |

---

## Benefits

✅ **One script** - No confusion  
✅ **Menu-driven** - Easy to use  
✅ **Auto-detects** - API key or not  
✅ **Flexible** - Choose your mode  
✅ **Simple** - Just run and select  

---

## That's It!

No complex setup, no multiple scripts, just:

```bash
python run.py
```

And choose what you want to do! 🚀

---

## Need Help?

- **For assignment**: Use Option 1 (regex mode)
- **For any PDF**: Use Option 2 (AI mode) 
- **For web demo**: Use Option 3 (web app)

**All in one script!** 🎉
