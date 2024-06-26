# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string



### absolute filters
#without these the word can't exists in the dictionary (vowels)

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The quick brown fox jumped over the lazy dog" #type your message here
print("Message:", message)

#create the Caesar cypher
offset = 5 #choose your shift
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        keys[letters[index]] = letters[(letters.index(letter) + offset) % totalLetters]
        invkeys[letters[(letters.index(letter) + offset) % totalLetters]] = letters[index]
    else: #uppercase
        keys[letters[index].upper()] = letters[((letters.index(letter) + offset) % totalLetters)].upper()
        invkeys[letters[((letters.index(letter) + offset) % totalLetters)].upper()] = letters[index].upper()

#encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list into string



#decrypt
decryptedMessage = []


for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string

