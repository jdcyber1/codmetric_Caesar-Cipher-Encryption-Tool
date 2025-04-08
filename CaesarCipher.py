import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def handle_encrypt():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        encrypted = encrypt(text, shift)

        encrypted_text.config(state='normal')
        encrypted_text.delete(1.0, tk.END)
        encrypted_text.insert(tk.END, encrypted)
        encrypted_text.config(state='disabled')

        copy_encrypt_btn.config(state="normal")

    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer.")

def handle_decrypt():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        decrypted = decrypt(text, shift)

        decrypted_text.config(state='normal')
        decrypted_text.delete(1.0, tk.END)
        decrypted_text.insert(tk.END, decrypted)
        decrypted_text.config(state='disabled')

        copy_decrypt_btn.config(state="normal")

    except ValueError:
        messagebox.showerror("Input Error", "Shift value must be an integer.")

def copy_encrypted():
    encrypted = encrypted_text.get(1.0, tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(encrypted)
    messagebox.showinfo("Copied", "Encrypted message copied to clipboard!")

def copy_decrypted():
    decrypted = decrypted_text.get(1.0, tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(decrypted)
    messagebox.showinfo("Copied", "Decrypted message copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("600x580")
root.resizable(False, False)

tk.Label(root, text="🔐 Caesar Cipher Tool", font=("Helvetica", 18, "bold")).pack(pady=10)

tk.Label(root, text="Enter Text:", font=("Helvetica", 12)).pack()
entry_text = tk.Entry(root, width=60, font=("Helvetica", 12))
entry_text.pack(pady=5)

tk.Label(root, text="Enter Shift Value (e.g., 3):", font=("Helvetica", 12)).pack()
entry_shift = tk.Entry(root, width=10, font=("Helvetica", 12))
entry_shift.pack(pady=5)

# Buttons for separate processing
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="🔐 Encrypt", command=handle_encrypt, font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="🔓 Decrypt", command=handle_decrypt, font=("Helvetica", 12)).grid(row=0, column=1, padx=10)

# Encrypted Section
tk.Label(root, text="Encrypted Message:", font=("Helvetica", 14, "bold")).pack()
encrypted_text = tk.Text(root, height=3, width=65, font=("Helvetica", 13), wrap="word", state="disabled")
encrypted_text.pack(pady=5)
copy_encrypt_btn = tk.Button(root, text="📋 Copy Encrypted", command=copy_encrypted, font=("Helvetica", 12), state="disabled")
copy_encrypt_btn.pack(pady=5)

# Decrypted Section
tk.Label(root, text="Decrypted Message:", font=("Helvetica", 14, "bold")).pack(pady=(10, 0))
decrypted_text = tk.Text(root, height=3, width=65, font=("Helvetica", 13), wrap="word", state="disabled")
decrypted_text.pack(pady=5)
copy_decrypt_btn = tk.Button(root, text="📋 Copy Decrypted", command=copy_decrypted, font=("Helvetica", 12), state="disabled")
copy_decrypt_btn.pack(pady=5)

root.mainloop()
