# Caesar Cipher Implementation
# Course: Information Security
# Lab Assignment 1
# Name: Your Name
# Roll Number: Your Roll Number

def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)

        # Check if character is lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)

        # Keep spaces and special characters unchanged
        else:
            encrypted_text += char

    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isupper():
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)

        elif char.islower():
            decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted_text += char

    return decrypted_text


# Main Program
if __name__ == "__main__":
    message = input("Enter message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    print("Encrypted Text:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted Text:", decrypted)
