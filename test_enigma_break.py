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

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "hail shakes"
crib_substring = ""
print(crib_substring)

class Iterator:
    def __init__(self):
        self.current = 'AAA'
    
    def next_iteration(self):
        if self.current == 'ZZZ':
            return None
        chars = list(self.current)
        for i in range(len(chars)-1, -1, -1):
            if chars[i] != 'Z':
                chars[i] = chr(ord(chars[i]) + 1)
                break
            else:
                chars[i] = 'A'
        self.current = ''.join(chars)
        return self.current
    
    def get_current(self):
        return self.current


Iterator = Iterator()
while True:
    
    key = Iterator.get_current()
    print(key)
    shakes_engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key=key,
                                plugs="AA BB CC DD EE")
    
    message = shakes_engine.encipher(ShakesHorribleMessage)
    print(message, key)
    if message.endswith("Hail Shakes!"):
        print(f"The decrypted message is: {message}")
        print(f"with a key of {key}")
        break
    
    next_key = Iterator.next_iteration()
    if next_key is None:
        print("Crib not found. Exiting loop.")
        break





        