import numpy as np
from PIL import Image
import uuid
import os

# to get image extension
def get_image_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lstrip('.')

# encrypt
def encrypt_image(image_path, key):
    img = Image.open(image_path)

    # image to numpy array
    img_array = np.array(img)
    # perform bitwise 
    img_array = np.bitwise_xor(img_array, key)
    # array to iimage
    img = Image.fromarray(img_array)

    # Save 
    image_name = f'encrypted_image_{uuid.uuid1()}.{get_image_extension(image_path)}'
    img.save(image_name)
    print('Encrypted Image saved as :', image_name)

# decrypt
def decrypt_image(image_path, key):
    img = Image.open(image_path)

    # image to a numpy array
    img_array = np.array(img)

    # perform bitwise to reverse encryption
    img_array = np.bitwise_xor(img_array, key)

    # array to image
    img = Image.fromarray(img_array)
    
    image_name = f'decrypted_image_{uuid.uuid1()}.{get_image_extension(image_path)}'
    img.save(image_name)
    print('Decrypted Image saved as :', image_name)

if __name__ == "__main__":
    while True:
        choice =  input('1. ENCRYPT IMAGE \n2. DECRYPT IMAGE\n')
        path = input('ENTER PATH : \n')
        while True:
            key = input('ENTER KEY : \n')
            if key.isdigit():
                key=int(key)
                break

        if choice == '1':
            encrypt_image(path, key)
        elif choice == '2':
            decrypt_image(path,key)