from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)
    np.random.seed(key)  # Deterministic for given key

    # Generate a random mask
    mask = np.random.randint(0, 256, size=arr.shape, dtype=np.uint8)
    encrypted_arr = (arr ^ mask)
    encrypted_img = Image.fromarray(encrypted_arr)
    encrypted_img.save(output_path)

def decrypt_image(input_path, output_path, key):
    # Same process as encryption (XOR is reversible)
    img = Image.open(input_path)
    arr = np.array(img)
    np.random.seed(key)
    mask = np.random.randint(0, 256, size=arr.shape, dtype=np.uint8)
    decrypted_arr = (arr ^ mask)
    decrypted_img = Image.fromarray(decrypted_arr)
    decrypted_img.save(output_path)