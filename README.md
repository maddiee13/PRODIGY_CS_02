# PixCryptor

Simple image encryption/decryption using pixel manipulation.

## Features
- Encrypt and decrypt images using a key and pixel-wise XOR with a random mask.
- Command-line and GUI interfaces.
- Cross-platform: Windows, Debian, Ubuntu.

## Usage

### Install
```bash
pip install -r requirements.txt
```

### CLI
```bash
python cli.py encrypt input.png encrypted.png 12345
python cli.py decrypt encrypted.png decrypted.png 12345
```

### GUI
```bash
python gui.py
```

## How it Works
- Uses a key to seed a random number generator.
- Generates a random mask (same shape as image).
- XORs mask with image pixels to encrypt/decrypt.
- Reversible: Encrypt again with the same key to decrypt.

PixCryptor Usage Guide
=====================

---
CLI Version
---

1. Install requirements:
   pip install -r requirements.txt

2. Show help and usage examples:
   python cli.py --help

   Example help output:
   -------------------
   PixCryptor: Simple image encryption/decryption tool.

   usage: cli.py {encrypt,decrypt} ...

   Examples:
     Encrypt: python cli.py encrypt input.png output.png 1234
     Decrypt: python cli.py decrypt encrypted.png output.png 1234

   Commands:
     encrypt   Encrypt an image
     decrypt   Decrypt an image

   Arguments for encrypt/decrypt:
     input     Input image path
     output    Output image path
     key       Encryption/Decryption key (number)

3. Encrypt an image:
   python cli.py encrypt input_image.png output_image.png 1234

4. Decrypt an image:
   python cli.py decrypt encrypted_image.png output_image.png 1234

---
GUI Version
---

1. Install requirements:
   pip install -r requirements.txt

2. Run the GUI:
   python Gui.py

3. In the GUI:
   - Click 'Browse...' to select an image file.
   - Enter a numeric key.
   - Choose 'Encrypt' or 'Decrypt'.
   - Click 'Run' and select where to save the output.

---
Notes
---
- Use the same key for decryption that you used for encryption.
- Supported image formats: PNG, JPG, JPEG, BMP.
- For CLI, colorized output will indicate success, info, and errors.
- For GUI, tooltips and progress bar enhance usability.