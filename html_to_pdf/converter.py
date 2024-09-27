import os
import pdfkit
from bs4 import BeautifulSoup

# Load the HTML template from the file
with open('<file>.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all containers
containers = soup.find_all(class_='container')

# Create a temporary directory for individual HTML files
os.makedirs('temp_html', exist_ok=True)

# Generate individual HTML files for each container
for i, container in enumerate(containers):
    with open(f'temp_html/page_{i + 1}.html', 'w') as temp_file:
        temp_file.write(str(container))  # Write only the container content

# Define options for PDF generation
options = {
    'page-size': 'A4',  # Adjust as needed
    'encoding': 'UTF-8',
    'margin-top': '10mm',
    'margin-right': '10mm',
    'margin-bottom': '10mm',
    'margin-left': '10mm',
}

# Generate PDF from individual HTML files
pdf_files = []
for i in range(len(containers)):
    pdf_file = f'temp_html/page_{i + 1}.pdf'
    pdfkit.from_file(f'temp_html/page_{i + 1}.html', pdf_file, options=options)
    pdf_files.append(pdf_file)

# Merge all PDFs into a single PDF file
from PyPDF2 import PdfMerger

merger = PdfMerger()
for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("output.pdf")
merger.close()

# Cleanup: Remove temporary HTML files
for i in range(len(containers)):
    os.remove(f'temp_html/page_{i + 1}.html')
    os.remove(f'temp_html/page_{i + 1}.pdf')

os.rmdir('temp_html')  # Remove the temporary directory
