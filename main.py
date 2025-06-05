import argparse
from PyPDF2 import PdfReader, PdfWriter


parser = argparse.ArgumentParser(description='Protect PDF with password.')
parser.add_argument('inputpdf',help='path to the PDF file to protect')
parser.add_argument('outputpdf',help='path to the output PDF file')
parser.add_argument('passwd',help='passwd to protect the PDF file')

args = parser.parse_args()