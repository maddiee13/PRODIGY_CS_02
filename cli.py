import argparse
from pixcryptor import encrypt_image, decrypt_image

def main():
    parser = argparse.ArgumentParser(description="PixCryptor: Simple image encryption/decryption tool.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt an image')
    encrypt_parser.add_argument('input', help='Input image path')
    encrypt_parser.add_argument('output', help='Output (encrypted) image path')
    encrypt_parser.add_argument('key', type=int, help='Encryption key (number)')

    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt an image')
    decrypt_parser.add_argument('input', help='Input (encrypted) image path')
    decrypt_parser.add_argument('output', help='Output (decrypted) image path')
    decrypt_parser.add_argument('key', type=int, help='Decryption key (same as used for encryption)')

    args = parser.parse_args()

    if args.command == 'encrypt':
        encrypt_image(args.input, args.output, args.key)
        print(f"Encrypted {args.input} -> {args.output} with key {args.key}")
    elif args.command == 'decrypt':
        decrypt_image(args.input, args.output, args.key)
        print(f"Decrypted {args.input} -> {args.output} with key {args.key}")

if __name__ == '__main__':
    main()