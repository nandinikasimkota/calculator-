import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = length_var.get()
    try:
        length = int(length)
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a positive integer.")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return

    password = [
        random.choice(string.ascii_uppercase) if use_upper else '',
        random.choice(string.ascii_lowercase) if use_lower else '',
        random.choice(string.digits) if use_digits else '',
        random.choice(string.punctuation) if use_special else '',
    ]
    password = [c for c in password if c]  # Remove empty strings

    while len(password) < length:
        password.append(random.choice(character_pool))

    random.shuffle(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, ''.join(password))

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.StringVar(value="12")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

# Widgets
tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(root, text="Password Length:").pack()
tk.Entry(root, textvariable=length_var).pack()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, font=("Helvetica", 12), justify='center')
password_entry.pack(pady=5, fill='x', padx=20)

root.mainloop()