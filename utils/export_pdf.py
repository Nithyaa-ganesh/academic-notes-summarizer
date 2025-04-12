from fpdf import FPDF
import os

def save_as_pdf(summary, flashcards, filename="summary_flashcards.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Summary Section
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, "Summary", ln=True)
    pdf.set_font("Arial", size=12)
    for line in summary.strip().split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.ln(5)

    # Flashcards Section
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, "Flashcards", ln=True)
    pdf.set_font("Arial", size=12)
    for line in flashcards.strip().split("\n"):
        pdf.multi_cell(0, 10, line)

    # Save to Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_path = os.path.join(downloads_path, filename)
    pdf.output(output_path)
    return output_path
