from flask import Flask, render_template, request, send_file, redirect, url_for
from PyPDF2 import PdfReader, PdfWriter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_pdf():
    if 'pdf' not in request.files or request.files['pdf'].filename == '':
        return "❌ No PDF uploaded."

    file = request.files['pdf']
    password = request.form.get('password')
    if not password:
        return "❌ Please enter a password."

    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_path)

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)

        output_filename = f"protected_{filename}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        with open(output_path, 'wb') as f:
            writer.write(f)

        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
