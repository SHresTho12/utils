import os
from PyPDF2 import PdfMerger

# Path to the folder containing PDF files
folder_path = '.'

# Create a PdfMerger object
merger = PdfMerger()

# List all PDF files in the folder
pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

# Sort PDF files if needed
pdf_files.sort()

# Loop through each PDF file and append it to the merger
for pdf_file in pdf_files:
    pdf_file_path = os.path.join(folder_path, pdf_file)
    merger.append(pdf_file_path)
    print(f"Added {pdf_file} to merger.")

# Path to save the merged PDF
merged_pdf_output_path = os.path.join(folder_path, 'merged_output.pdf')

# Write the merged PDF to a file
merger.write(merged_pdf_output_path)
merger.close()

print(f"Merged PDF saved at {merged_pdf_output_path}")
