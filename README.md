# PDFPass - PDF Password Protection Tool

## Overview

**PDFPass** is a simple tool to protect your PDF files with a password.  
You can use it in two ways:
- **Web Version:** Use a modern, neon-themed web interface to upload and protect your PDFs.
- **CLI Version:** Use the command line to quickly encrypt PDFs.

---

## 🌐 Web Version

Access the tool online at:  
[https://pdfpass-1.onrender.com/](https://pdfpass-1.onrender.com/)

Or run it locally:

```sh
# Clone the repository and install dependencies
git clone https://github.com/yourusername/pdfpass.git
cd pdfpass
pip install -r requirements.txt

# Start the web server
python web_app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 💻 CLI Version

Encrypt a PDF directly from your terminal:

```sh
python main.py -i input.pdf -o output.pdf -p yourpassword
```

- `-i` or `--inputpdf`: Path to the PDF file you want to protect.
- `-o` or `--outputpdf`: Path for the password-protected output PDF.
- `-p` or `--passwd`: Password to set on the PDF.

**Example:**
```sh
python main.py -i myfile.pdf -o myfile_protected.pdf -p secret123
```

---

## Features

- 🔒 Password-protect any PDF file
- 🖥️ Easy-to-use web interface
- ⚡ Fast command-line encryption
- 🟢 Neon hacker-style web design

---

## Requirements

- Python 3.7+
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Flask](https://pypi.org/project/Flask/) (for web version)

Install dependencies:
```sh
pip install -r requirements.txt
```

---

## License

MIT License

---

## Credits

Made by