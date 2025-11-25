"""
Setup script for AI-powered version
Helps you configure Groq API key
"""

import os
import sys


def setup_groq_api():
    """Interactive setup for Groq API key"""
    print("=" * 70)
    print("AI-Powered Document Extraction - Setup")
    print("=" * 70)
    print()
    
    # Check if API key already set
    existing_key = os.environ.get("GROQ_API_KEY")
    if existing_key:
        print(f"✓ GROQ_API_KEY already set: {existing_key[:10]}...")
        response = input("\nDo you want to update it? (y/n): ")
        if response.lower() != 'y':
            print("\n✓ Using existing API key")
            return existing_key
    
    print("\n📝 Get your FREE Groq API key:")
    print("   1. Go to: https://console.groq.com")
    print("   2. Sign up (free)")
    print("   3. Go to 'API Keys' section")
    print("   4. Click 'Create API Key'")
    print("   5. Copy your API key")
    print()
    
    api_key = input("Enter your Groq API key: ").strip()
    
    if not api_key:
        print("\n❌ No API key provided")
        return None
    
    # Set environment variable for current session
    os.environ["GROQ_API_KEY"] = api_key
    
    print("\n✓ API key set for current session")
    print()
    print("To make it permanent:")
    print()
    
    if sys.platform == "win32":
        print("Windows PowerShell:")
        print(f'  $env:GROQ_API_KEY="{api_key}"')
        print()
        print("Windows CMD:")
        print(f'  set GROQ_API_KEY={api_key}')
        print()
        print("Or add to System Environment Variables:")
        print("  1. Search 'Environment Variables' in Windows")
        print("  2. Click 'Environment Variables'")
        print("  3. Add new variable: GROQ_API_KEY")
    else:
        print("Mac/Linux:")
        print(f'  export GROQ_API_KEY="{api_key}"')
        print()
        print("Add to ~/.bashrc or ~/.zshrc to make permanent:")
        print(f'  echo \'export GROQ_API_KEY="{api_key}"\' >> ~/.bashrc')
    
    print()
    return api_key


def test_api_connection(api_key):
    """Test if API key works"""
    print("\n🧪 Testing API connection...")
    
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        
        # Simple test
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Say 'API works!'"}],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✓ API Response: {result}")
        print("✓ Connection successful!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nPlease check:")
        print("  1. API key is correct")
        print("  2. You have internet connection")
        print("  3. Groq service is available")
        return False


def main():
    """Main setup function"""
    api_key = setup_groq_api()
    
    if not api_key:
        print("\n❌ Setup cancelled")
        return
    
    # Test connection
    if test_api_connection(api_key):
        print("\n" + "=" * 70)
        print("✅ Setup Complete!")
        print("=" * 70)
        print()
        print("You can now run:")
        print("  python extract_data_ai.py")
        print()
        print("This will extract data from ANY PDF document using AI!")
        print("=" * 70)
    else:
        print("\n❌ Setup failed - please check your API key")


if __name__ == "__main__":
    main()
