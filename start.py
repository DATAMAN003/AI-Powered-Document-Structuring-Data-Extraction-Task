"""
Simple Startup Script - Just run this!
Checks API key and starts web server
"""

import os
import sys
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def main():
    print("=" * 70)
    print("🚀 AI Document Extraction - Starting Web Server")
    print("=" * 70)
    print()
    
    # Check API key
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key or api_key.strip() == "":
        print("❌ ERROR: Groq API key not found!")
        print()
        print("Please set up your API key:")
        print()
        print("1. Get FREE API key: https://console.groq.com")
        print("2. Open .env file in this folder")
        print("3. Add your key after GROQ_API_KEY=")
        print("4. Save and run this script again")
        print()
        print("Example .env file:")
        print("  GROQ_API_KEY=gsk_your_actual_key_here")
        print()
        sys.exit(1)
    
    print("✅ API key found!")
    print()
    print("🌐 Starting web server...")
    print("📍 Access at: http://localhost:5000")
    print()
    print("Features:")
    print("  • Upload ANY PDF document")
    print("  • AI-powered intelligent extraction")
    print("  • Download structured Excel output")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    print()
    
    # Start Flask app
    from app import app
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
        sys.exit(0)
