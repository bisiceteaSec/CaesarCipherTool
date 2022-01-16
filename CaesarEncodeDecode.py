import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(textF, shiftF):
    endText = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'decode':
                shiftF *= -1
            newPosition = position + shiftF

            while newPosition > 25:
                newPosition -= 26
            while newPosition < 0:
                newPosition += 26
            newLetter = alphabet[newPosition]
            endText += newLetter
        else:
            endText += letter
    print(f"Answer: {endText}")

print(art.logo)
continueProgram = True
while continueProgram:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        continueProgram = False