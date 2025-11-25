"""
UNIFIED DOCUMENT EXTRACTION SYSTEM
One script to run everything - Simple and Easy!
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def check_setup():
    """Check if everything is set up correctly"""
    print("=" * 70)
    print("🚀 Document Extraction System - Unified Runner")
    print("=" * 70)
    print()
    
    # Check for API key
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key or api_key == "your_api_key_here" or api_key.strip() == "":
        print("⚠️  Groq API key not configured")
        print()
        print("To use AI-powered extraction:")
        print("1. Get FREE API key: https://console.groq.com")
        print("2. Open .env file")
        print("3. Replace 'your_api_key_here' with your actual key")
        print()
        print("For now, using regex-based extraction (works great!)")
        print()
        return False
    else:
        print("✅ Groq API key found - AI mode available!")
        print()
        return True


def show_menu():
    """Show user menu"""
    print("\n" + "=" * 70)
    print("What would you like to do?")
    print("=" * 70)
    print()
    print("1. Extract data from PDF (Regex - Fast, for assignment)")
    print("2. Extract data from PDF (AI - Intelligent, any document)")
    print("3. Run web application (Upload interface)")
    print("4. Exit")
    print()


def extract_regex():
    """Run regex-based extraction"""
    print("\n" + "=" * 70)
    print("📄 Regex-Based Extraction (Fast & Accurate)")
    print("=" * 70)
    
    from extract_data_enhanced import EnhancedDocumentExtractor
    
    pdf_file = input("\nEnter PDF filename (or press Enter for 'Data Input.pdf'): ").strip()
    if not pdf_file:
        pdf_file = "Data Input.pdf"
    
    if not os.path.exists(pdf_file):
        print(f"\n❌ Error: {pdf_file} not found")
        return
    
    output_file = input("Enter output filename (or press Enter for 'Output.xlsx'): ").strip()
    if not output_file:
        output_file = "Output.xlsx"
    
    print(f"\n🔄 Processing {pdf_file}...")
    
    try:
        extractor = EnhancedDocumentExtractor(pdf_file)
        text = extractor.extract_text_from_pdf()
        print(f"✓ Extracted {len(text)} characters")
        
        data = extractor.identify_key_value_pairs()
        print(f"✓ Identified {len(data)} data entries")
        
        extractor.export_to_excel(output_file)
        print(f"\n✅ Success! Output saved to: {output_file}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")


def extract_ai():
    """Run AI-based extraction"""
    print("\n" + "=" * 70)
    print("🤖 AI-Powered Extraction (Intelligent & Flexible)")
    print("=" * 70)
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key.strip() == "":
        print("\n❌ Groq API key not configured!")
        print("\nPlease:")
        print("1. Get FREE API key: https://console.groq.com")
        print("2. Open .env file")
        print("3. Add your API key")
        print("4. Run this script again")
        return
    
    from extract_data_ai import AIDocumentExtractor
    
    pdf_file = input("\nEnter PDF filename (or press Enter for 'Data Input.pdf'): ").strip()
    if not pdf_file:
        pdf_file = "Data Input.pdf"
    
    if not os.path.exists(pdf_file):
        print(f"\n❌ Error: {pdf_file} not found")
        return
    
    output_file = input("Enter output filename (or press Enter for 'Output_AI.xlsx'): ").strip()
    if not output_file:
        output_file = "Output_AI.xlsx"
    
    print(f"\n🔄 Processing {pdf_file} with AI...")
    
    try:
        extractor = AIDocumentExtractor(pdf_file, groq_api_key=api_key)
        
        text = extractor.extract_text_from_pdf()
        print(f"✓ Extracted {len(text)} characters")
        
        data = extractor.analyze_document_with_ai()
        print(f"✓ AI extracted {len(data)} data entries")
        
        extractor.export_to_excel(output_file)
        print(f"\n✅ Success! Output saved to: {output_file}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("- Check your API key in .env file")
        print("- Ensure you have internet connection")
        print("- Verify Groq service is available")


def run_web_app():
    """Run Flask web application"""
    print("\n" + "=" * 70)
    print("🌐 Starting Web Application")
    print("=" * 70)
    print()
    print("Web server starting...")
    print("Access at: http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    
    # Import and run Flask app
    from app import app
    app.run(debug=False, host='0.0.0.0', port=5000)


def main():
    """Main function"""
    has_api_key = check_setup()
    
    while True:
        show_menu()
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            extract_regex()
        elif choice == "2":
            if has_api_key:
                extract_ai()
            else:
                print("\n⚠️  AI extraction requires Groq API key")
                print("Using regex extraction instead...")
                extract_regex()
        elif choice == "3":
            run_web_app()
            break  # Exit after web app closes
        elif choice == "4":
            print("\n👋 Goodbye!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter 1-4")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
