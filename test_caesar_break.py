# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

from break_caesar import *




message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
#assuming space isn't a key
letter_counts[" "] = -1
for letter, freq in letter_counts.items(): 
    #print(letter, ":", freq) 
    #INSERT CODE TO REMEMBER MAX
    if maxFreq < freq:
        maxFreq = freq
        maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

"""
Determines the shirt based on a letter and the maxLetter in ascii characters

"""
def get_shift(letter: str, MaxLetter: str):
    LetterIndex = letters.index(letter)
    MaxLetterIndex = letters.index(MaxLetter)
    return abs(MaxLetterIndex - LetterIndex) % 26

def decrypt_caesar(message: str, shift):
    decryptedMessage = []
    totalLetters = 26
    invkeys = {} 
    for index, letter in enumerate(letters):
        # cypher setup
        if index < totalLetters: #lowercase
            invkeys[letters[(letters.index(letter) + shift) % totalLetters]] = letters[index]
        else: #uppercase
            invkeys[letters[((letters.index(letter) + shift) % totalLetters)].upper()] = letters[index].upper()

    for letter in message:
        if letter == ' ': #spaces
            decryptedMessage.append(letter)
        else:
            decryptedMessage.append(invkeys[letter])
    return ''.join(decryptedMessage)

shift = get_shift("e", maxLetter)
print("Predicted Shift:", shift)

#uses the assumption that e is the most abundant character
e_ass = decrypt_caesar(message, shift)



#uses the assumption tha e is not the most abundant character
non_e_ass = find_max_similarity_message(message)




