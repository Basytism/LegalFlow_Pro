import customtkinter as ctk
from tkinter import filedialog
from logic import fill_contract, export_pdf, generate_template

class Dashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="white")

        self.title = ctk.CTkLabel(self, text="📑 LegalFlow Pro – Dashboard", font=("Segoe UI", 24, "bold"))
        self.title.pack(pady=30)

        # Browse Contracts Button
        self.browse_btn = ctk.CTkButton(
            self,
            text="📂 Browse Contract Template",
            command=self.browse_contract
        )
        self.browse_btn.pack(pady=10)

        # Fill Contract Button
        self.fill_btn = ctk.CTkButton(
            self,
            text="📝 Fill Contract",
            command=fill_contract.fill_existing_template
        )
        self.fill_btn.pack(pady=10)

        # Generate Contract From Form Button
        self.generate_btn = ctk.CTkButton(
            self,
            text="🧾 Create Contract from Form",
            command=generate_template.create_contract_from_form
        )
        self.generate_btn.pack(pady=10)

        # Export to PDF Button
        self.export_btn = ctk.CTkButton(
            self,
            text="📤 Export Filled Contract to PDF",
            command=export_pdf.export_to_pdf
        )
        self.export_btn.pack(pady=10)

    def browse_contract(self):
        file_path = filedialog.askopenfilename(
            title="Select a DOCX Contract Template",
            filetypes=[("Word Documents", "*.docx")]
        )
        if file_path:
            print("Selected template:", file_path)

