def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def main():
    mode = input("Do you want to encrypt or decrypt? ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift number: "))

    result = caesar_cipher(text, shift, mode)
    print(f"The {mode}ed text is: {result}")

if __name__ == "__main__":
    main()
