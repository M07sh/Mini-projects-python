from art import logo_caesar
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

length_of_alphabet = len(alphabet)
print(logo_caesar)
answer = "yes"


def caesar(words,shifting,dire):
  caesar_word = ""
  
  shifting%=length_of_alphabet
  if dire == "decode":
    shifting*=-1
  for letters in words:
    if letters not in alphabet:
      caesar_word+=letters
    else:
      new_index = alphabet.index(letters) + shifting
      if new_index >= length_of_alphabet:
        new_index -= (length_of_alphabet)
      new_letter = alphabet[new_index]

      
      caesar_word+=new_letter
  
  print(f"The {dire}d text is {caesar_word}")



while answer != "no":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(words = text,shifting = shift,dire = direction)
  answer = input("do you want to restart?")

  
