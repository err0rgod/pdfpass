from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from PyPDF2 import PdfReader, PdfWriter
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages

# === Config ===
UPLOAD_FOLDER = "uploads"
PROTECTED_FOLDER = "protected"
ALLOWED_EXTENSIONS = {'pdf'}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# === Ensure folders exist ===
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROTECTED_FOLDER, exist_ok=True)

# === Helper Functions ===
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def cleanup_files(*paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)

# === Routes ===
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'pdf' not in request.files:
            flash("❌ No file part.")
            return redirect(request.url)

        file = request.files['pdf']
        password = request.form['password']

        if file.filename == "":
            flash("❌ No file selected.")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Generate safe random filenames
            filename = secure_filename(file.filename)
            unique_id = uuid.uuid4().hex
            input_path = os.path.join(UPLOAD_FOLDER, f"{unique_id}_{filename}")
            output_path = os.path.join(PROTECTED_FOLDER, f"protected_{unique_id}_{filename}")

            try:
                file.save(input_path)

                reader = PdfReader(input_path)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                writer.encrypt(password)

                with open(output_path, 'wb') as f:
                    writer.write(f)

                response = send_file(output_path, as_attachment=True)

                # Cleanup after sending
                cleanup_files(input_path, output_path)

                return response

            except Exception as e:
                flash(f"❌ Error: {e}")
                cleanup_files(input_path, output_path)
                return redirect(request.url)

        else:
            flash("❌ Invalid file type. Only PDF allowed.")
            return redirect(request.url)

    return render_template("index.html")



if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print("🔥 Server crashed with exception:")
        traceback.print_exc()
