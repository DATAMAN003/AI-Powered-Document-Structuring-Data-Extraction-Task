"""
Test AI extraction to make sure it works
"""

import os
from dotenv import load_dotenv
from extract_data_ai import AIDocumentExtractor

# Load .env
load_dotenv()

def test_extraction():
    print("=" * 70)
    print("Testing AI Extraction")
    print("=" * 70)
    print()
    
    # Check API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key.strip() == "":
        print("❌ ERROR: GROQ_API_KEY not set in .env file")
        print("\nPlease:")
        print("1. Open .env file")
        print("2. Add your API key: GROQ_API_KEY=your_key_here")
        print("3. Run this test again")
        return
    
    print(f"✅ API key found: {api_key[:10]}...")
    print()
    
    # Test extraction
    pdf_file = "Data Input.pdf"
    if not os.path.exists(pdf_file):
        print(f"❌ ERROR: {pdf_file} not found")
        return
    
    print(f"📄 Processing: {pdf_file}")
    print()
    
    try:
        # Create extractor
        extractor = AIDocumentExtractor(pdf_file, groq_api_key=api_key)
        
        # Extract text
        print("[1/3] Extracting text...")
        text = extractor.extract_text_from_pdf()
        print(f"✓ Extracted {len(text)} characters")
        print()
        
        # AI analysis
        print("[2/3] AI analyzing...")
        data = extractor.analyze_document_with_ai()
        print(f"✓ Extracted {len(data)} entries")
        print()
        
        # Show sample data
        if data:
            print("Sample entries:")
            for i, entry in enumerate(data[:3]):
                print(f"\n  Entry {i+1}:")
                print(f"    Category: {entry.get('Category', 'N/A')}")
                print(f"    Key: {entry.get('Key', 'N/A')}")
                print(f"    Value: {entry.get('Value', 'N/A')}")
                print(f"    Comments: {entry.get('Comments', 'N/A')[:50]}...")
        
        print()
        
        # Export to Excel
        print("[3/3] Creating Excel...")
        output_file = "Test_Output.xlsx"
        extractor.export_to_excel(output_file)
        print(f"✓ Excel created: {output_file}")
        print()
        
        # Summary
        print("=" * 70)
        print("✅ TEST PASSED!")
        print("=" * 70)
        print(f"Total entries: {len(data)}")
        print(f"Output file: {output_file}")
        print()
        print("Categories:")
        categories = {}
        for entry in data:
            cat = entry.get('Category', 'Uncategorized')
            categories[cat] = categories.get(cat, 0) + 1
        for cat, count in categories.items():
            print(f"  • {cat}: {count} entries")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_extraction()
