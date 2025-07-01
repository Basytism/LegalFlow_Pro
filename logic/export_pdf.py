from docx2pdf import convert
from tkinter import filedialog
import os
import customtkinter as ctk

def export_to_pdf():
    # Ask user to select a filled Word document
    docx_path = filedialog.askopenfilename(
        title="Select a Filled .docx Contract",
        filetypes=[("Word Documents", "*.docx")]
    )

    if not docx_path:
        return

    # Ask where to save the PDF
    save_dir = filedialog.askdirectory(title="Select Output Folder for PDF")
    if not save_dir:
        return

    try:
        convert(docx_path, os.path.join(save_dir, os.path.basename(docx_path).replace(".docx", ".pdf")))
        ctk.CTkMessagebox(title="Success", message="📄 Contract exported to PDF successfully.")
    except Exception as e:
        ctk.CTkMessagebox(title="Error", message=f"❌ Failed to export: {e}")
