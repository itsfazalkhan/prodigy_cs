import tkinter as tk

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def encrypt_text():
    shift = int(encrypt_shift_entry.get())
    encrypted_text = encrypt(encrypt_text_entry.get(), shift)
    encrypt_result_label.config(text="Encrypted Text: " + encrypted_text)

def decrypt_text():
    shift = int(decrypt_shift_entry.get())
    decrypted_text = decrypt(decrypt_text_entry.get(), shift)
    decrypt_result_label.config(text="Decrypted Text: " + decrypted_text)

# Creating the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption and Decryption")

# Adding some padding between frames
root.rowconfigure(0, minsize=200, weight=1)
root.columnconfigure([0, 1], minsize=200, weight=1)

# Creating frames for encryption and decryption columns
encrypt_frame = tk.Frame(root, bg="#f0f0f0")
encrypt_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

decrypt_frame = tk.Frame(root, bg="#f0f0f0")
decrypt_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Encryption section
encrypt_heading_label = tk.Label(encrypt_frame, text="Encryption", font=("Arial", 14, "bold"), bg="#f0f0f0")
encrypt_heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

encrypt_text_label = tk.Label(encrypt_frame, text="Enter text:", font=("Arial", 12), bg="#f0f0f0")
encrypt_text_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
encrypt_text_entry = tk.Entry(encrypt_frame, width=20, font=("Arial", 12))
encrypt_text_entry.grid(row=1, column=1, padx=10, pady=5)

encrypt_shift_label = tk.Label(encrypt_frame, text="Enter shift value:", font=("Arial", 12), bg="#f0f0f0")
encrypt_shift_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
encrypt_shift_entry = tk.Entry(encrypt_frame, width=5, font=("Arial", 12))
encrypt_shift_entry.grid(row=2, column=1, padx=10, pady=5)

encrypt_button = tk.Button(encrypt_frame, text="Encrypt", command=encrypt_text, font=("Arial", 12), bg="#4CAF50", fg="white")
encrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

encrypt_result_label = tk.Label(encrypt_frame, text="", font=("Arial", 12), bg="#f0f0f0")
encrypt_result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Decryption section
decrypt_heading_label = tk.Label(decrypt_frame, text="Decryption", font=("Arial", 14, "bold"), bg="#f0f0f0")
decrypt_heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

decrypt_text_label = tk.Label(decrypt_frame, text="Enter text:", font=("Arial", 12), bg="#f0f0f0")
decrypt_text_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
decrypt_text_entry = tk.Entry(decrypt_frame, width=20, font=("Arial", 12))
decrypt_text_entry.grid(row=1, column=1, padx=10, pady=5)

decrypt_shift_label = tk.Label(decrypt_frame, text="Enter shift value:", font=("Arial", 12), bg="#f0f0f0")
decrypt_shift_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
decrypt_shift_entry = tk.Entry(decrypt_frame, width=5, font=("Arial", 12))
decrypt_shift_entry.grid(row=2, column=1, padx=10, pady=5)

decrypt_button = tk.Button(decrypt_frame, text="Decrypt", command=decrypt_text, font=("Arial", 12), bg="#FF5733", fg="white")
decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

decrypt_result_label = tk.Label(decrypt_frame, text="", font=("Arial", 12), bg="#f0f0f0")
decrypt_result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Running the main loop
root.mainloop()
