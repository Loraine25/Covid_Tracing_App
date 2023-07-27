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

# Create a bordered frame to contain all the widgets
        main_frame = ttk.Frame(root, style='Medical.TFrame')
        main_frame.pack(padx=20, pady=20)

# Labels and Entry widgets for input
        name_label = tk.Label(main_frame, text="Full Name:", font=font_style)
        name_label.grid(row=0, column=0, pady=10)
        self.name_var = tk.StringVar()
        name_entry = tk.Entry(main_frame, textvariable=self.name_var, font=font_style)
        name_entry.grid(row=0, column=1, pady=10)

        phone_label = tk.Label(main_frame, text="Phone Number:", font=font_style)
        phone_label.grid(row=1, column=0, pady=10)
        self.phone_var = tk.StringVar()
        phone_entry = tk.Entry(main_frame, textvariable=self.phone_var, font=font_style)
        phone_entry.grid(row=1, column=1, pady=10)

        date_label = tk.Label(main_frame, text="Date of Contact (YYYY-MM-DD):", font=font_style)
        date_label.grid(row=2, column=0, pady=10)
        self.date_var = tk.StringVar()
        date_entry = tk.Entry(main_frame, textvariable=self.date_var, font=font_style)
        date_entry.grid(row=2, column=1, pady=10)

        location_label = tk.Label(main_frame, text="Location of Contact:", font=font_style)
        location_label.grid(row=3, column=0, pady=10)
        self.location_var = tk.StringVar()
        location_entry = tk.Entry(main_frame, textvariable=self.location_var, font=font_style)
        location_entry.grid(row=3, column=1, pady=10)

# Add Entry button
        add_button = tk.Button(main_frame, text="Add Entry", command=self.add_entry, font=font_style)
        add_button.grid(row=5, column=0, columnspan=2, pady=10)

# Search Entry section
        search_label = tk.Label(main_frame, text="Search:", font=font_style)
        search_label.grid(row=6, column=0, pady=10)
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(main_frame, textvariable=self.search_var, font=font_style)
        search_entry.grid(row=6, column=1, pady=10)

# Search Criteria Radiobuttons
        self.search_criteria_var = tk.StringVar()
        self.search_criteria_var.set("Name")  # Default search criteria
        search_criteria_frame = ttk.Frame(main_frame, style='Medical.TFrame')
        search_criteria_frame.grid(row=7, column=0, columnspan=2, pady=10)

        name_radio = tk.Radiobutton(search_criteria_frame, text="Name", variable=self.search_criteria_var,
                                    value="Name", font=font_style)
        name_radio.pack(side=tk.LEFT, padx=5)

        phone_radio = tk.Radiobutton(search_criteria_frame, text="Phone", variable=self.search_criteria_var,
                                     value="Phone", font=font_style)
        phone_radio.pack(side=tk.LEFT, padx=5)

# Search Button
        search_button = tk.Button(main_frame, text="Search", command=self.search_entry, font=font_style)
        search_button.grid(row=8, column=0, columnspan=2, pady=10)

