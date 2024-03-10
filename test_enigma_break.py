# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "hail shakes"
crib_substring = ""
print(crib_substring)

class Iterator:
    def __init__(self):
        self._rotor_count = 3
        self.permutations = pow(26, self._rotor_count) - 1 # Represents 'ZZZ', or the start of 'AAAA'.
        self.current_number = self.permutations  # Start from the maximum.

    def next_iteration(self):
        self.current_number -= 1  # Decrement 'number' for the next iteration.

    def get_current(self):
        # Adjust to 0-based for calculation
        number = self.current_number - 1
        chars = []
        for index in range (self._rotor_count):
            number, remainder = divmod(number, 26)
            # Fix the off-by-one error by adjusting remainder
            chars.append(chr(ord('A') + remainder))
        return ''.join(reversed(chars)) if chars else 'A'  # Ensure 'A' is returned for the first position

    def get_iterations(self):
        return self.permutations - self.current_number
    
    def check_end(self): 
        return self.current_number <= 1


start = time.time()
Iterator = Iterator()

while True:
    key = Iterator.get_current()
    #print(key)
    shakes_engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key=key,
                                plugs="AA BB CC DD EE")
    
    message = shakes_engine.encipher(ShakesHorribleMessage)
    #print(message, key)

    if message.endswith("Hail Shakes!"):
        print(f"The decrypted message is: {message}")
        print(f"with a key of {key}")
        print(Iterator.get_iterations())
        break
    
    Iterator.next_iteration()
    if Iterator.check_end() is True:
        print("Crib not found. Exiting loop.")
        break

end = time.time()
print(end - start)





        