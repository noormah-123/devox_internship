def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:
                result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Get input from the user
message = input("Enter a message: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message
encrypted_message = caesar_encrypt(message, shift)

# Decrypt the message
decrypted_message = caesar_decrypt(encrypted_message, shift)

# Display results
print("\nCAESAR CIPHER RESULTS")
print("---------------------")
print("Original message :", message)
print("Shift value      :", shift)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)