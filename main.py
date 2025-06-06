import argparse
from PyPDF2 import PdfReader, PdfWriter


parser = argparse.ArgumentParser(description='Protect PDF with password.')
parser.add_argument('inputpdf',help='path to the PDF file to protect')
parser.add_argument('outputpdf',help='path to the output PDF file')
parser.add_argument('passwd',help='passwd to protect the PDF file')

args = parser.parse_args()


try :
    reader = PdfReader(args.inputpdf)

except FileNotFoundError:
    print(f"Error: The file '{args.inputpdf}' does not exist.")
    exit(1)

except Exception as e:
    print(f"Error occurred while reading the PDF file: {e}")
    exit(1)


writer = PdfWriter()
for pager in reader.pages:
    writer.add_page(pager)

writer.encrypt(args.password)


try:
    with open(args.output_pdf, 'wb') as output_file:
        writer.write(output_file)
    print("✅ Encrypted PDF saved successfully!")
except Exception as e:
    print(f"❌ Failed to write output file: {e}")


