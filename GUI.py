import tkinter as tk
from tkinter import ttk

class ContactTracingAppGUI:
    def __init__(self, root):
        root.title("COVID Contact Tracing App")
        root.configure(bg="#E8F5FE")

        # Define the formal cursive font and border style
        font_style = ("Monotype Corsiva", 14, "italic")
        border_style = ttk.Style()
        border_style.configure('Medical.TFrame', background='white', borderwidth=2, relief='ridge')
