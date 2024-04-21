import tkinter as tk
from tkinter import ttk
import random
import string
import sys

# Dictionary mapping the country code to the license plate format
license_plate_formats = {
    'AT': 'U-####',
    'BE': '1-###-###',
    'BG': 'CA ####',
    'HR': 'HR-##-CCC',
    'CY': 'CY ####',
    'CZ': '1A####',
    'DK': 'AB ## ###',
    'EE': 'ABC-####',
    'FI': 'AAA-###',
    'FR': '1AA-###-AA',
    'DE': 'B-####',
    'GR': 'AA ####',
    'HU': 'ABC-###',
    'IE': '1O-####-A',
    'IT': 'AA ####',
    'LV': 'AA####',
    'LT': 'ABC ###',
    'LU': '1BB-####',
    'MT': '1AA-####',
    'NL': '1-T-###-T',
    'PL': 'UA ####',
    'PT': '1-##-##-##',
    'RO': 'HR-##-CCC',
    'SK': 'TT ## TT',
    'SI': 'AA-####',
    'ES': 'AA ####',
    'SE': 'ABC ###'
}

# Dictionary mapping the country code to the country name
country_mapping = {
    'AT': 'Austria',
    'BE': 'Belgium',
    'BG': 'Bulgaria',
    'HR': 'Croatia',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DK': 'Denmark',
    'EE': 'Estonia',
    'FI': 'Finland',
    'FR': 'France',
    'DE': 'Germany',
    'GR': 'Greece',
    'HU': 'Hungary',
    'IE': 'Ireland',
    'IT': 'Italy',
    'LV': 'Latvia',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'MT': 'Malta',
    'NL': 'Netherlands',
    'PL': 'Poland',
    'PT': 'Portugal',
    'RO': 'Romania',
    'SK': 'Slovakia',
    'SI': 'Slovenia',
    'ES': 'Spain',
    'SE': 'Sweden'
}

# Variables to store the last generated license plate and country
last_license_plate = ""
last_country = ""

# Function to generate a random European-style license plate
def generate_license_plate(country_code):
    format_string = license_plate_formats.get(country_code, 'U-####')
    license_plate = ''
    for char in format_string:
        if char == '#':
            license_plate += random.choice(string.digits)
        elif char == 'A':
            license_plate += random.choice(string.ascii_uppercase)
        elif char == 'U':
            license_plate += random.choice(string.ascii_uppercase + string.digits)
        else:
            license_plate += char
    country = country_mapping.get(country_code, 'Unknown')
    return license_plate, country

# Function to update the license plate label, country label, and EU flag label
def update_license_plate():
    country_code = country_combobox.get()
    global last_license_plate, last_country
    last_license_plate, last_country = generate_license_plate(country_code)
    license_plate_label.config(text=last_license_plate)
    country_label.config(text=f"Country: {last_country}")

# Function to randomly generate a license plate from the selected country
def generate_from_selected_country():
    country_code = country_combobox.get()
    license_plate, country_name = generate_license_plate(country_code)
    license_plate_label.config(text=license_plate)
    country_label.config(text=f"Country: {country_name}")

# Function to exit the application
def exit_application():
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("European License Plate Generator")

# Create a frame to hold the content
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a label to display the license plate
license_plate_label = ttk.Label(frame, text="", font=("Arial", 24))
license_plate_label.grid(row=0, column=0, padx=10, pady=10)

# Create a label to display the country
country_label = ttk.Label(frame, text="", font=("Arial", 16))
country_label.grid(row=1, column=0, padx=10, pady=5)

# Create a Combobox to select a country
country_combobox = ttk.Combobox(frame, values=list(country_mapping.keys()), state="readonly", font=("Arial", 12))
country_combobox.grid(row=2, column=0, padx=10, pady=10)
country_combobox.set("Choose a country")

# Load the EU flag image
eu_flag_image = tk.PhotoImage(file="eu_flag.png")

# Create a label to display the EU flag image
eu_flag_label = ttk.Label(frame, image=eu_flag_image)
eu_flag_label.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

# Create a "Generate" button to randomly show a license plate from the selected country
generate_button = ttk.Button(frame, text="Generate", command=generate_from_selected_country)
generate_button.grid(row=3, column=0, padx=10, pady=10)

# Create an exit button with modified appearance
exit_button = ttk.Button(frame, text="Exit", command=exit_application, style="TButton")
exit_button.grid(row=4, column=0, padx=10, pady=10)

# Style configuration for the exit button
style = ttk.Style()
style.configure("TButton", font=("Arial", 14), foreground="red", background="white")

# Run the main loop
root.mainloop()
