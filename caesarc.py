def caesarcipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


if __name__ == '__main__':
    print("Caesar Cipher")
    message = input("Enter message: ")
    try:
        shift = int(input("Shift no? "))
    except ValueError:
        print("Invalid shift; using 0.")
        shift = 0

    shift = shift % 26
    mode = input("Do you want to encrypt or decrypt? ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        print("Unknown mode; defaulting to encrypt.")
        mode = "encrypt"

    output = caesarcipher(message, shift, mode)
    print("\nResult:", output)