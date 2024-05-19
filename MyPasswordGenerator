# Generator de parole 18.03.24 B Florea
# zNx8W%Ij 
# exemplu mai sus

# Module necesare
import tkinter as tk
from tkinter import messagebox
import random
import string

# Functie generare parola
def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Nu pot fi introudse numere negative")
    except ValueError as ve:
        messagebox.showerror("Mai incearca", f"Error: {ve}")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

# Functie copiat parola
def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Done", "Parola copiata")
    else:
        messagebox.showwarning("Eroare", "Nu a fost generata parola!")

# Fereastra principala
root = tk.Tk()
root.title("Generator Parole")

# Setare dimensiune fereastra
root.geometry("300x400")

# Create and place widgets
tk.Label(root, text="Introduceti numarul de caractere:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generare Parola", command=generate_password).pack(pady=10)
tk.Button(root, text="Copiere", command=copy_to_clipboard).pack(pady=10)

# Buton iesire cu stilizare
exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#ff6666", fg="white")
exit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Mainloop
root.mainloop()
