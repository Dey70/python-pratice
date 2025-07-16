alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_location= alphabet.index(letter) + shift_amount
        shifted_location %= len(alphabet)  # Wrap around if it exceeds the length of the alphabet
        cipher_text += alphabet[shifted_location]
    print(f"The encoded text is {cipher_text}")
encrypt(original_text=text, shift_amount=shift)

