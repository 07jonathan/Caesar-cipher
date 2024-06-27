def atbash_cipher(text):
    # Create a dictionary to map each letter to its Atbash equivalent
    atbash_dict = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_alphabet = alphabet[::-1]
    
    # Fill the dictionary with mappings for uppercase letters
    for i in range(len(alphabet)):
        atbash_dict[alphabet[i]] = reversed_alphabet[i]
    
    # Fill the dictionary with mappings for lowercase letters
    alphabet = alphabet.lower()
    reversed_alphabet = reversed_alphabet.lower()
    for i in range(len(alphabet)):
        atbash_dict[alphabet[i]] = reversed_alphabet[i]
    
    # Convert the input text using the Atbash cipher
    cipher_text = ''
    for char in text:
        if char in atbash_dict:
            cipher_text += atbash_dict[char]
        else:
            cipher_text += char  # Non-alphabet characters remain unchanged
    
    return cipher_text

# Example usage
plaintext = "Hello, World!"
ciphertext = atbash_cipher(plaintext)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
