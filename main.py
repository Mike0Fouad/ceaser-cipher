from styling import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again= True
#encryption function by shifting forward by the shift number and text
def encrypt_decrypt(text,shift, direction):
    if direction == "decode":
        shift *= -1
    elif direction != "encode" or direction != "decode":
        print("Please enter a valid direction")
    encrypted_text = ""
    #loop through text
    for letter in text:
        # return letters shifted
        if letter in alphabet:
            new_letter = (alphabet.index(letter) + shift) % len(alphabet)
            encrypted_text += alphabet[new_letter]
        #return non alphabet letters as is
        else:
            encrypted_text += letter
    #return encrypted_decypted text
    return encrypted_text

print(logo)
print("Welcome to Caesar Cipher\n This program will encrypt or decrypt your message by shifting the letters by a number you choose.\n")
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(encrypt_decrypt(text=text,shift=shift,direction=direction))
    another = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if another == "no":
        again = False
        print(Goodbye)

            