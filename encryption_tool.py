import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Function to generate and save the encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select File to Encrypt")
    if not file_path:
        return

    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)

    messagebox.showinfo("Success", f"File Encrypted: {encrypted_file_path}")

# Function to decrypt a file
def decrypt_file():
    file_path = filedialog.askopenfilename(title="Select File to Decrypt")
    if not file_path or not file_path.endswith(".enc"):
        messagebox.showerror("Error", "Invalid File Selected!")
        return

    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    decrypted_file_path = file_path.replace(".enc", "")
    with open(decrypted_file_path, "wb") as file:
        file.write(decrypted_data)

    messagebox.showinfo("Success", f"File Decrypted: {decrypted_file_path}")

# Create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Advanced Encryption Tool")
    root.geometry("400x200")

    label = tk.Label(root, text="AES-256 File Encryption Tool", font=("Arial", 14))
    label.pack(pady=10)

    encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file, bg="green", fg="white")
    encrypt_button.pack(pady=5)

    decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file, bg="blue", fg="white")
    decrypt_button.pack(pady=5)

    root.mainloop()

# Generate key only once
if not os.path.exists("secret.key"):
    generate_key()

# Run GUI
create_gui()
