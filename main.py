import argparse   # for command line intraction
from PyPDF2 import PdfReader, PdfWriter     #for reading and writing with pdf



#getting command line input from user
parser = argparse.ArgumentParser(description='Protect PDF with password.')
parser.add_argument('-i', '--inputpdf', help='path to the PDF file to protect')
parser.add_argument('-o', '--outputpdf', help='path to the output PDF file')
parser.add_argument('-p', '--passwd', help='passwd to protect the PDF file')

args = parser.parse_args() 

#checking for user provided input and doing some error handling
#and opening and reading the pdf
try :
    reader = PdfReader(args.inputpdf)

except FileNotFoundError:
    print(f"Error: The file '{args.inputpdf}' does not exist.")
    exit(1)

except Exception as e:
    print(f"Error occurred while reading the PDF file: {e}")
    exit(1)


#writing the pdf with new password with writer.encrypt 

writer = PdfWriter()
for pager in reader.pages:
    writer.add_page(pager)

writer.encrypt(args.passwd)


#firse error handling for wrriting part

try:
    with open(args.outputpdf, 'wb') as output_file:
        writer.write(output_file)
    print("✅ Encrypted PDF saved successfully!")
except Exception as e:
    print(f"❌ Failed to write output file: {e}")


