###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    if char.isalpha(): 
        if char.islower():
            offset = ord('a')
        else:
            offset = ord('A')

        original_position = ord(char) - offset
        new_position = (original_position + 1) % 26
        new_char = chr(new_position + offset)
    # add one to the character's code
    # replace new character code with its
    # corresponding character (use chr())
    # add encrypted character to encrypted text
        encrypted_text += new_char

    else:
        encrypted_text += char



print(plain_text)
print(encrypted_text)