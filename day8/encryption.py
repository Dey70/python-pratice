alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caear_cipher(original_text, shift_amount, encode_or_decode):
    plain_text = "" 
    for letter in original_text:
        if encode_or_decode == "decode":
            shifted_amount *= -1
        shifted_location = alphabet.index(letter) + shift_amount
        shifted_location %= len(alphabet)
        plain_text += alphabet[shifted_location]

    print(f"The {encode_or_decode}d text is {plain_text}")

decrypt(original_text=text, shift_amount=shift, encode_or_decode=direction)
