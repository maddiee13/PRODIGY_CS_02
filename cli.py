import argparse
from pixcryptor import encrypt_image, decrypt_image
import sys
from colorama import init, Fore, Style
import os
import time

init(autoreset=True)

def print_success(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def print_error(msg):
    print(Fore.RED + msg + Style.RESET_ALL)

def print_info(msg):
    print(Fore.CYAN + msg + Style.RESET_ALL)

def spinner(msg, duration=1):
    print_info(msg)
    for _ in range(duration):
        for c in '|/-\\':
            sys.stdout.write(f'\r{c}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r')
    sys.stdout.flush()

def main():
    parser = argparse.ArgumentParser(
        description="PixCryptor: Simple image encryption/decryption tool.",
        epilog="""
Examples:
  Encrypt: python cli.py encrypt input.png output.png 1234
  Decrypt: python cli.py decrypt encrypted.png output.png 1234
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
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

    try:
        if not os.path.isfile(args.input):
            print_error(f"Input file not found: {args.input}")
            sys.exit(1)
        if args.command == 'encrypt':
            spinner("Encrypting image...")
            encrypt_image(args.input, args.output, args.key)
            print_success(f"Encrypted {args.input} -> {args.output} with key {args.key}")
        elif args.command == 'decrypt':
            spinner("Decrypting image...")
            decrypt_image(args.input, args.output, args.key)
            print_success(f"Decrypted {args.input} -> {args.output} with key {args.key}")
        print_info("Operation completed successfully.")
    except Exception as e:
        print_error(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()