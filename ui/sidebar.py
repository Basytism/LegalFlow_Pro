import customtkinter as ctk
from PIL import Image, ImageTk
import os

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=200, fg_color="#F4F4F4")

        # Logo image
        logo_path = os.path.join("assets", "synergy_logo.png")
        if os.path.exists(logo_path):
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize((50, 50))
            logo_tk = ImageTk.PhotoImage(logo_image)
            self.logo_label = ctk.CTkLabel(self, image=logo_tk, text="", fg_color="transparent")
            self.logo_label.image = logo_tk
            self.logo_label.pack(pady=(20, 10))
        
        # App title
        self.title_label = ctk.CTkLabel(
            self, 
            text="LegalFlow Pro", 
            font=("Segoe UI", 16, "bold"),
            text_color="#333"
        )
        self.title_label.pack(pady=(0, 20))

        # Placeholder for sidebar buttons
        self.modules_label = ctk.CTkLabel(
            self, 
            text="Sidebar Modules",
            font=("Segoe UI", 12),
            text_color="#777"
        )
        self.modules_label.pack(pady=(0, 10))

        # Future buttons can go here
        # e.g., Settings, History, Help, etc.

