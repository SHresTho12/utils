import json
from fpdf import FPDF

# Initialize the PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Load the JSON file
with open('bl_data.json') as json_file:
    products = json.load(json_file)

# Function to add a new page and write data
def add_product_page(product):
    pdf.add_page()

    # Set font for the page
    pdf.set_font("Arial", size=12)

    # Write each key-value pair from the JSON object to the PDF
    for key, value in product.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

# Loop through all products and add them to individual pages
for product in products:
    add_product_page(product)

# Output the PDF to a file
pdf_output_path = 'product_catalog.pdf'
pdf.output(pdf_output_path)

print(f"PDF generated: {pdf_output_path}")
