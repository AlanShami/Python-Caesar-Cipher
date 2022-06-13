from art import logo
from art import alphabet

print(logo)

def caesar(start_text, shift_key, cipher_mode):
  end_text = ""
  
  if cipher_mode == "decode":
    shift_key *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_key
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_mode}d result: {end_text}")

should_end = False

while not should_end:

  mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  while not mode == "encode" or mode == "decode":
    mode = input("Type either 'encode' or 'decode':\n")
    
  text = input("Type your message:\n").lower()
  key = input("Type the shift number:\n")

  while not key.isdigit():
    key = input("The shift has to be a whole number:\n")

  key = int(key)
 
  key = key % 26

  caesar(start_text=text, shift_key=key, cipher_mode=mode)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("goodbye")
    

