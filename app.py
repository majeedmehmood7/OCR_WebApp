from flask import Flask, request, render_template, send_from_directory
import os
import pytesseract
from PIL import Image

# Specify the Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return render_template('index.html', error='No file uploaded')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No file selected')
    
    if file:
        # Save the uploaded image
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        print(f"Image saved at: {filepath}")  # Debug print
        
        # Perform OCR
        try:
            image = Image.open(filepath)
            text = pytesseract.image_to_string(image)
            return render_template('index.html', text=text, filename=file.filename)
        except Exception as e:
            return render_template('index.html', error=f'Error processing image: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)