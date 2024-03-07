
from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Apply a basic mathematical operation to each pixel using the key
    encrypted_array = img_array + key

    # Create a new image from the encrypted NumPy array
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(encrypted_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_path)

    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img)

    # Reverse the encryption using the key
    decrypted_array = encrypted_array - key

    # Clip values to stay within valid pixel range (0-255)
    decrypted_array = np.clip(decrypted_array, 0, 255)

    # Create a new image from the decrypted NumPy array
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")

# Example Usage:
# Replace 'your_image.jpg' with the path to your image file
image_path = 'your_image.jpg'
encryption_key = 50

# Encrypt the image
encrypt_image(image_path, encryption_key)

# Decrypt the image
decrypt_image("encrypted_image.png", encryption_key)
