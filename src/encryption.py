
# Basic Encryption and Decryption
# Technique: Caesar Cipher

def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            shifted_char = chr(
                (ord(char) - start + shift) % 26 + start
            )

            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
print("===== ENCRYPTION AND DECRYPTION TOOL =====")

message = input("Enter the text: ")
shift = int(input("Enter the shift key: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\n----- RESULTS -----")
print("Original Text:", message)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
