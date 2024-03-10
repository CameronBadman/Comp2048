# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

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
    """
    Determines the shift used in the Caesar Cipher based on a given letter and the maxLetter.
    
    Parameters:
    - letter: The letter to compare to the maxLetter.
    - MaxLetter: The most frequently occurring letter in the message.
    
    Returns:
    - The calculated shift as an integer.
    """
    LetterIndex = letters.index(letter)
    MaxLetterIndex = letters.index(MaxLetter)
    return abs(MaxLetterIndex - LetterIndex) % 26

def decrypt_caesar(message: str, shift):
    """
    Decrypts a message encrypted with a Caesar Cipher using a given shift.
    
    Parameters:
    - message: The encrypted message as a string.
    - shift: The shift used in the Caesar Cipher as an integer.
    
    Returns:
    - The decrypted message as a string.
    """
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

"""

"""
data = {
    "e": 11.16071,
    "a": 8.4966,
    "r": 7.5809,
    "i": 7.5448,
    "o": 7.1635,
    "t": 6.9509,
    "n": 6.6544,
    "s": 5.7351,
    "l": 5.4893,
    "c": 4.5388,
    "u": 3.6308,
    "d": 3.3844,
    "p": 3.1671,
    "h": 3.0034,
    "g": 2.4705,
    "b": 2.0720,
    "f": 1.8121,
    "y": 1.7779,
    "w": 1.2899,
    "k": 1.1016,
    "v": 1.0074,
    "x": 0.2902,
    "z": 0.2722,
    "j": 0.1965,
    "q": 0.1962
}

def letter_frequency(message):
    """
    Calculates the frequency of each letter in a message.
    
    Parameters:
    - message: The message for which to calculate letter frequencies.
    
    Returns:
    - A dictionary of letter frequencies in percentage.
    """
    """Calculate the frequency of each letter in the message."""
    message = message.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    letter_counts = Counter(message)
    total_letters = sum(letter_counts.values())
    return {letter: (count / total_letters) * 100 for letter, count in letter_counts.items()}

def find_max_similarity_message(message, data):
    """
    Finds the decrypted message that has the maximum similarity to typical English letter frequencies.
    
    Parameters:
    - message: The encrypted message as a string.
    - data: A dictionary of typical English letter frequencies.
    
    Returns:
    - The best decrypted message as a string and the corresponding shift as an integer.
    """
    best_shift = None
    best_similarity = float('-inf')
    decrypted_message_best = ""
    
    for shift in range(26):
        decrypted_message = decrypt_caesar(message, shift)
        decrypted_freq = letter_frequency(decrypted_message)
        
        # Calculate similarity to English frequencies
        similarity = sum(min(decrypted_freq.get(letter, 0), frequency) for letter, frequency in data.items())
        
        if similarity > best_similarity:
            best_similarity = similarity
            best_shift = shift
            decrypted_message_best = decrypted_message
            
    return decrypted_message_best, best_shift

decrypted_message, shift = find_max_similarity_message(message, data)
print("Decrypted Message:", decrypted_message)
print("Best Shift:", shift)
