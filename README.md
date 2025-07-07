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