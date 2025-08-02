OCR Web App
A simple yet powerful web application built with Python and Flask that allows users to upload images and extract text using Optical Character Recognition (OCR) powered by Tesseract. The app features an attractive user interface, image display, and a reset option to clear results.
Description
This project is an OCR-based web tool designed to convert text from uploaded images into editable text. It uses the Tesseract OCR engine integrated with Python's pytesseract library and serves the application via a Flask web framework. The interface is styled with CSS for a modern and creative look, including animations and a responsive design.
Features

Upload images (PNG, JPG, etc.) and extract text.
Display the uploaded image and extracted text on the web page.
Reset functionality to clear the form and results.
Attractive UI with gradient backgrounds, animations, and interactive buttons.
Runs locally for development and testing.

Requirements

Python 3.12.6
Tesseract OCR (installed on the system)
Required Python packages:

flask
pytesseract
pillow



Installation
Prerequisites

Install Python 3.12.6 from python.org.
Install Tesseract OCR for Windows from GitHub and add it to your system PATH (e.g., C:\Program Files\Tesseract-OCR).

Verify installation by running tesseract --version in Command Prompt.

Setup
git clone https://github.com/yourusername/OCR_WebApp.git
cd OCR_WebApp

Create a virtual environment and activate it:
python -m venv venv
.\venv\Scripts\activate

Install the required packages:
pip install flask pytesseract pillow

Update the Tesseract path in app.py if needed (e.g., pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe').

Run the application:
python app.py

Project Structure
OCR_WebApp/
├── app.py           # Flask application logic
├── templates/       # HTML templates
│   └── index.html   # Main web page
├── static/          # CSS and static files
│   └── styles.css   # Styling for the app
├── uploads/         # Folder for uploaded images
└── venv/            # Virtual environment (optional)

License
This project is open-source and available under the MIT License (add a LICENSE file if desired).
Acknowledgments

Tesseract OCR by Google for the core OCR functionality.
Flask framework for the web application.
Inspiration from creative web design communities.
