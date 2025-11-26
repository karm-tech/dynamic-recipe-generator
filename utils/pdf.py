from fpdf import FPDF
from io import BytesIO

def generate_pdf(title: str, ingredients: list, instructions: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(0, 10, txt=title, ln=True, align='C')
    pdf.ln(10)

    # Ingredients
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(0, 10, "Ingredients:", ln=True)
    pdf.set_font("Arial", size=11)
    for ing in ingredients:
        pdf.multi_cell(0, 8, f"• {ing}")
    pdf.ln(5)

    # Instructions
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(0, 10, "Instructions:", ln=True)
    pdf.set_font("Arial", size=11)
    steps = instructions.split("\n")
    for step in steps:
        if step.strip():
            pdf.multi_cell(0, 8, step.strip())
            pdf.ln(1)
    
    # Footer
    pdf.set_font("Arial", size=10, style='')
    pdf.ln(10)
    pdf.cell(0, 10, "Made by DRG 4.0", ln=True, align='R')

    buffer = BytesIO()
    # Output to buffer as string (latin-1) and encode to bytes, or use dest='S' if supported by version
    # Standard fpdf approach for bytes buffer:
    pdf_content = pdf.output(dest='S').encode('latin-1')
    buffer.write(pdf_content)
    buffer.seek(0)
    return buffer
