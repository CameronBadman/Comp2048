# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import enigma
import rotor

engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AA BB CC DD EE")


def reset_engine():
    engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AA BB CC DD EE")
reset_engine()
#print(engine)

# Part a)
message = "Hello World"
print("Message:", message)
secret = engine.encipher(message)
print("Encoded Message (Part A):", secret)

reset_engine()

# Decrypt the message
decrypted_message = engine.encipher(secret)  # Re-encrypt the ciphertext to decrypt it
print("Decrypt Message (Part A):", decrypted_message)

#Part b)
ShakesHorribleMessage = "Vxye ajgh D yf? Ptn uluo yjgco L ws nznde czidn. Bsj ccj qdbk qjph wpw ypxvu!"

shakes_engine = engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="SSC",
                                plugs="AA BB CC DD EE")

Message_decrpted = engine.encipher(ShakesHorribleMessage)

print (ShakesHorribleMessage + "\n" + Message_decrpted)
