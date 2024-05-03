import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global original_image
        original_image = Image.open(file_path)
        original_image.thumbnail((250, 250))
        img_original = ImageTk.PhotoImage(original_image)
        label_original.config(image=img_original)
        label_original.image = img_original

def encrypt_image():
    global selected_image
    if original_image:
        key = entry_key.get()
        if key:
            np.random.seed(int(key))
            key_array = np.random.randint(256, size=original_image.size[0]*original_image.size[1]*3, dtype=np.uint8)
            key_array = key_array.reshape(original_image.size[1], original_image.size[0], 3)
            selected_image = np.array(original_image)
            selected_image ^= key_array
            selected_image = Image.fromarray(selected_image)
            selected_image.thumbnail((250, 250))
            img_encrypted = ImageTk.PhotoImage(selected_image)
            label_encrypted.config(image=img_encrypted)
            label_encrypted.image = img_encrypted

def decrypt_image():
    global selected_image
    if selected_image:
        key = entry_key.get()
        if key:
            np.random.seed(int(key))  # Ensure the same key is generated
            key_array = np.random.randint(256, size=original_image.size[0]*original_image.size[1]*3, dtype=np.uint8)
            key_array = key_array.reshape(original_image.size[1], original_image.size[0], 3)
            selected_image = np.array(selected_image)
            selected_image ^= key_array
            selected_image = Image.fromarray(selected_image)
            selected_image.thumbnail((250, 250))
            img_decrypted = ImageTk.PhotoImage(selected_image)
            label_decrypted.config(image=img_decrypted)
            label_decrypted.image = img_decrypted

# Create main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Create labels for previews
label_original = tk.Label(root)
label_original.grid(row=0, column=0, padx=10, pady=10)
label_encrypted = tk.Label(root)
label_encrypted.grid(row=0, column=1, padx=10, pady=10)
label_decrypted = tk.Label(root)
label_decrypted.grid(row=0, column=2, padx=10, pady=10)

# Create buttons and entry for key
button_browse = tk.Button(root, text="Browse for Image", command=browse_image)
button_browse.grid(row=1, column=0, padx=10, pady=10)
button_encrypt = tk.Button(root, text="Encrypt Image", command=encrypt_image)
button_encrypt.grid(row=1, column=1, padx=10, pady=10)
button_decrypt = tk.Button(root, text="Decrypt Image", command=decrypt_image)
button_decrypt.grid(row=1, column=2, padx=10, pady=10)

entry_key_label = tk.Label(root, text="Symmetric Key:")
entry_key_label.grid(row=2, column=0, padx=10, pady=5)
entry_key = tk.Entry(root)
entry_key.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

# Initialize global variable for selected image
original_image = None
selected_image = None

root.mainloop()
