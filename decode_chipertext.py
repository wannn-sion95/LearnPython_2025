def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


chiper_text = str(input("Masukkan Chiper Text: "))

plaintext = caesar_cipher(chiper_text, 13)

print("Cipher Text: ", chiper_text)
print("Hasil: ", plaintext)
