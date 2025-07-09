import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Added for themed widgets
from pixcryptor import encrypt_image, decrypt_image
import os

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x, y, _, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 20
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", 8, "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

class PixCryptorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PixCryptor")
        self.input_path = ""
        self.key = tk.StringVar()
        self.mode = tk.StringVar(value="encrypt")

        # Set window icon if available
        icon_path = "icon.ico"
        if os.path.exists(icon_path):
            try:
                self.root.iconbitmap(icon_path)
            except Exception:
                pass
        self.root.resizable(False, False)

        # Main frame
        main_frame = ttk.Frame(root, padding="20 15 20 15")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Title label
        title_label = ttk.Label(main_frame, text="PixCryptor", font=("Segoe UI", 18, "bold"), foreground="#3366cc")
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

        # Image file
        ttk.Label(main_frame, text="Image File:").grid(row=1, column=0, sticky="e", padx=(0, 5), pady=5)
        self.input_entry = ttk.Entry(main_frame, width=40)
        self.input_entry.grid(row=1, column=1, pady=5)
        browse_btn = ttk.Button(main_frame, text="Browse...", command=self.browse_file)
        browse_btn.grid(row=1, column=2, padx=(5, 0), pady=5)
        ToolTip(browse_btn, "Select an image file to encrypt or decrypt.")

        # Key
        ttk.Label(main_frame, text="Key (number):").grid(row=2, column=0, sticky="e", padx=(0, 5), pady=5)
        key_entry = ttk.Entry(main_frame, textvariable=self.key, width=20)
        key_entry.grid(row=2, column=1, sticky="w", pady=5)
        ToolTip(key_entry, "Enter a numeric key for encryption/decryption.")

        # Mode
        mode_frame = ttk.Frame(main_frame)
        mode_frame.grid(row=3, column=0, columnspan=3, pady=5)
        encrypt_rb = ttk.Radiobutton(mode_frame, text="Encrypt", variable=self.mode, value="encrypt")
        decrypt_rb = ttk.Radiobutton(mode_frame, text="Decrypt", variable=self.mode, value="decrypt")
        encrypt_rb.grid(row=0, column=0, padx=5)
        decrypt_rb.grid(row=0, column=1, padx=5)
        ToolTip(encrypt_rb, "Encrypt the selected image.")
        ToolTip(decrypt_rb, "Decrypt the selected image.")

        # Run button
        run_btn = ttk.Button(main_frame, text="Run", command=self.run)
        run_btn.grid(row=4, column=1, pady=15)
        ToolTip(run_btn, "Run encryption or decryption.")

        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode="indeterminate", length=200)
        self.progress.grid(row=5, column=0, columnspan=3, pady=(0, 5))
        self.progress.grid_remove()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.input_path = file_path
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def run(self):
        if not self.input_entry.get():
            messagebox.showerror("Error", "Select an image file.")
            return
        self.input_path = self.input_entry.get()
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
            self.progress.grid()
            self.progress.start(10)
            self.root.update_idletasks()
            if self.mode.get() == "encrypt":
                encrypt_image(self.input_path, out_path, key_val)
            else:
                decrypt_image(self.input_path, out_path, key_val)
            self.progress.stop()
            self.progress.grid_remove()
            messagebox.showinfo("Success", f"Output saved: {out_path}")
        except Exception as e:
            self.progress.stop()
            self.progress.grid_remove()
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = PixCryptorGUI(root)
    root.mainloop()