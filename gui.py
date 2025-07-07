import tkinter as tk
from tkinter import filedialog, messagebox
from pixcryptor import encrypt_image, decrypt_image
import os

class PixCryptorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PixCryptor")
        self.input_path = ""
        self.key = tk.StringVar()
        self.mode = tk.StringVar(value="encrypt")

        # Widgets
        tk.Label(root, text="Image File:").grid(row=0, column=0, sticky="e")
        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.grid(row=0, column=1)
        tk.Button(root, text="Browse...", command=self.browse_file).grid(row=0, column=2)

        tk.Label(root, text="Key (number):").grid(row=1, column=0, sticky="e")
        tk.Entry(root, textvariable=self.key, width=20).grid(row=1, column=1, sticky="w")

        tk.Radiobutton(root, text="Encrypt", variable=self.mode, value="encrypt").grid(row=2, column=0)
        tk.Radiobutton(root, text="Decrypt", variable=self.mode, value="decrypt").grid(row=2, column=1, sticky="w")

        tk.Button(root, text="Run", command=self.run).grid(row=3, column=1, pady=10)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.input_path = file_path
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def run(self):
        if not self.input_path:
            messagebox.showerror("Error", "Select an image file.")
            return
        try:
            key_val = int(self.key.get())
        except ValueError:
            messagebox.showerror("Error", "Key must be a number.")
            return

        out_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if not out_path:
            return
        try:
            if self.mode.get() == "encrypt":
                encrypt_image(self.input_path, out_path, key_val)
            else:
                decrypt_image(self.input_path, out_path, key_val)
            messagebox.showinfo("Success", f"Output saved: {out_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = PixCryptorGUI(root)
    root.mainloop()