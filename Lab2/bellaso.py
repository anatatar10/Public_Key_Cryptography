
def bellaso_decrypt(msg, key):
    ''' INPUT: str (encrypted), key (used w tabula recta to decrypt)
        OUTPUT: str (decrypted)
    '''
    decrypted = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    offset = 0
    # for-loop over every position in the message
    for ix in range(len(msg)):
        if msg[ix] not in alph: #  if the character is not in the alphabet ( it's a non-alphabetic character like whitespace or punctuation)
            output = msg[ix] # just return the original character (whitespace or punctuation)
            offset += -1 # increment offset, bcs the non-alphabetic characters don't affect the shifting

        # otherwise if the position wraps longer than len(alpha)
        elif (alph.find(msg[ix])) > (len(alph) - (alph.find(key[((ix + offset) % len(key))])) - 1):  # If the position requires wrapping around the alphabet,
            # finds the index of the character from the msg in the alph and compares it to the maximum index (position) in the alphabet where wrapping occurs when subtracting the key position.

            # If the position requires wrapping around the alphabet,
            # decrypt the character based on the keyword and apply modulo to handle wrapping.
            output = alph[(alph.find(msg[ix]) - (alph.find(key[((ix + offset) % len(key))]))) % 26]

        # else is same as previous case, but no wrapping so no modulo operation
        else:
            output = alph[alph.find(msg[ix]) - (alph.find(key[((ix + offset) % len(key))]))]
            # decrypted character by finding the position of the character in the message, adding the corresponding position in the key (with adjustments for wrapping),
            # and then ensuring that the result stays within the bounds of the alphabet by taking the modulo 26.
        decrypted += output
    return decrypted


def bellaso_encrypt(msg, key):
    ''' INPUT: str (unencrypted), key (used w tabula recta to encrypt)
        OUTPUT: str (encrypted)
    '''
    encoded = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    offset = 0
    for ix in range(len(msg)): # for-loop over every position in the message

        # and if it's not an alpha w correspondence
        if msg[ix] not in alph: #  if the character is not in the alphabet ( it's a non-alphabetic character like whitespace or punctuation)
            output = msg[ix] # just return the original character (whitespace or punctuation)
            offset += -1 # increment offset, bcs the non-alphabetic characters don't affect the shifting
        # otherwise if the position wraps longer than length of alphabet,
        elif (alph.find(msg[ix])) > (len(alph) - (alph.find(key[((ix + offset) % len(key))])) - 1): # If the position requires wrapping around the alphabet,
            #finds the index of the character from the msg in the alph and compares it to the maximum index (position) in the alphabet where wrapping occurs when subtracting the key position.

            # If the position requires wrapping around the alphabet,
            # decrypt the character based on the keyword and apply modulo to handle wrapping.
            output = alph[(alph.find(msg[ix]) + (alph.find(key[((ix + offset) % len(key))]))) % 26]
            # decrypted character by finding the position of the character in the message, adding the corresponding position in the key (with adjustments for wrapping),

        # else is same as previous case, but no wrapping so no modulo operation
        else:
            output = alph[alph.find(msg[ix]) + (alph.find(key[((ix + offset) % len(key))]))]
            # decrypted character by finding the position of the character in the message, adding the corresponding position in the key (with adjustments for wrapping),
            # and then ensuring that the result stays within the bounds of the alphabet by taking the modulo 26.

        encoded += output #add the encrypted characters together
    return encoded



chosen_keyword = 'toddlovescopper'
to_decrypt = 'Nxwwkpf jrw qt ndy jxsv\nYrff ielwfpa ffnbgdcwzw\nLahs\'h drv aossj uvqw\n'

decrypted_msg = bellaso_decrypt(to_decrypt, chosen_keyword)
print('\n')
print("Message to decrypt: ", to_decrypt)
print(f'\nDEcryption:\n{decrypted_msg}')

to_encrypt = 'your message here!'
keyword = 'chooseyourownadventure'
print('\n')
encrypted_msg = bellaso_encrypt(to_encrypt, keyword)
print("Message to encrypt: ", to_encrypt);
print(f'ENcryption: {encrypted_msg}\n')

# Ask the user to choose a keyword for encryption/decryption
chosen_keyword = input("Enter the keyword: ")

# Ask the user whether they want to encrypt or decrypt
choice = input("Do you want to encrypt or decrypt (e/d)? ").lower()

if choice == 'e':
    # Encryption
    to_encrypt = input("Enter the message to encrypt: ")
    encrypted_msg = bellaso_encrypt(to_encrypt, chosen_keyword)
    print("\nEncrypted Message:")
    print(encrypted_msg)
elif choice == 'd':
    # Decryption
    to_decrypt = input("Enter the message to decrypt: ")
    decrypted_msg = bellaso_decrypt(to_decrypt, chosen_keyword)
    print("\nDecrypted Message:")
    print(decrypted_msg)
else:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
