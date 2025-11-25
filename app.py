"""
AI-Powered Document Extraction Web Application
Simple web interface - Always uses AI for intelligent extraction
"""

from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from extract_data_ai import AIDocumentExtractor
import tempfile
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'ai-document-extraction-secret-key-2024'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Main page with upload form"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle PDF upload and process with AI extraction"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Save uploaded file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f'input_{timestamp}_{filename}')
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f'output_{timestamp}.xlsx')
        
        file.save(input_path)
        
        try:
            # Get API key
            api_key = os.getenv('GROQ_API_KEY')
            if not api_key or api_key.strip() == '':
                return jsonify({'error': 'API key not configured. Please set GROQ_API_KEY in .env file'}), 500
            
            print(f"\n🔄 Processing {filename}...")
            
            # Process with AI
            extractor = AIDocumentExtractor(input_path, groq_api_key=api_key)
            
            # Extract text
            print("  📄 Extracting text from PDF...")
            text = extractor.extract_text_from_pdf()
            print(f"  ✓ Extracted {len(text)} characters")
            
            # AI Analysis
            print("  🤖 AI analyzing document...")
            data = extractor.analyze_document_with_ai()
            print(f"  ✓ AI extracted {len(data)} entries")
            
            if not data or len(data) == 0:
                return jsonify({'error': 'No data extracted. Please check your PDF content.'}), 500
            
            # Export to Excel
            print("  📊 Creating Excel file...")
            extractor.export_to_excel(output_path)
            print(f"  ✓ Excel created: {output_path}")
            
            # Get statistics
            categories = {}
            for entry in data:
                cat = entry.get('Category', 'Uncategorized')
                categories[cat] = categories.get(cat, 0) + 1
            
            return jsonify({
                'success': True,
                'total_entries': len(data),
                'categories': categories,
                'download_url': f'/download/{os.path.basename(output_path)}'
            })
        
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
            return jsonify({'error': f'Extraction failed: {str(e)}'}), 500
        
        finally:
            # Clean up input file
            if os.path.exists(input_path):
                os.remove(input_path)
    
    return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400


@app.route('/download/<filename>')
def download_file(filename):
    """Download the generated Excel file"""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name='Extracted_Data.xlsx')
    return jsonify({'error': 'File not found'}), 404


@app.route('/demo')
def demo():
    """Demo page with sample data"""
    try:
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            return "Demo requires API key. Please set GROQ_API_KEY in .env file", 500
        
        extractor = AIDocumentExtractor("Data Input.pdf", groq_api_key=api_key)
        text = extractor.extract_text_from_pdf()
        data = extractor.analyze_document_with_ai()
        
        categories = {}
        for entry in data:
            cat = entry.get('category', 'Uncategorized')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(entry)
        
        return render_template('demo.html', categories=categories, total=len(data))
    except Exception as e:
        return f"Error loading demo: {str(e)}", 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
