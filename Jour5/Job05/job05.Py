message = input("Entrer message: ")

def caesar_shift(message, shift):
   result = ""
   for char in message:
       if char.isalpha():
           ascii_offset = ord('a') if char.islower() else ord('A')
           result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
       else:
           result += char
   return result

print(caesar_shift(message, 1))