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
    def __init__(self, rotor_count):
        self._rotor_count = rotor_count
        self.permutations = pow(26, self._rotor_count) - 1 # Represents 'ZZZ', or the start of 'AAAA'.
        self.current_number = self.permutations

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

def break_engigma(): 

    iterator_index = Iterator(3)

    while True:
        key = iterator_index.get_current()
        #print(key)
        shakes_engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                    rotor.ROTOR_II, rotor.ROTOR_III, key=key,
                                    plugs="AA BB CC DD EE")
        
        message = shakes_engine.encipher(ShakesHorribleMessage)
        #print(message, key)
        print(message, key)
        if message.endswith("Hail Shakes!"):
            print(f"The decrypted message is: {message}")
            print(f"with a key of {key}")
            print(f"number of attempts: {iterator_index.get_iterations()}")
            break
        
        iterator_index.next_iteration()
        if iterator_index.check_end() is True:
            print("Crib not found. Exiting loop.")
            break


start = time.time()
break_engigma()
end = time.time()
print(end - start)



#########################
#Q3D
"""
 if I were to make a guess, under the assumption of only using the crib "heil shakes" it would take around a hour to 12 hours minimum, a month at maximum. 

 https://brilliant.org/wiki/enigma-machine/#:~:text=Alan%20Turing%20and%20Gordon%20Welchman,send%20a%20given%20coded%20message.

 this source says that the Bombe machine was able to crack enigma in 20 mins. which is pretty similar to the 1 - 12 hours guess I gave, as the Bombe machine didn't just use "hail hitler", but also normally used "weather report" 
 the Bombe had 36 enigma machines running at once

"""

#Q3e
"""
with the extra rotors the extra amounts of permuations of the rotors alone is 5 x 4 x 3 = 60
plus the rotors of 26 ^ 3 = 17576 
the number of plugboard combinations is ~150,000,000,000,000 assuming all 10 pairs 

meaning that by the time you add all these numbers together 
you get 
158184000000000000000


assuming worst case all possible combinations, 

my computer burnt thought 5803 in 2.1246650218963623 as of writing this. 

as such 

https://plus.maths.org/content/exploring-enigma#:~:text=The%20answer%20is%20that%20there,letters%20on%20the%20plug%20board.


time_per_comptation is = 2.1246650218963623 / 5803 = 0.0003661321767872415

number of seconds for all possible combination

5.791625225291301e+16

5.79462089351128e+18 or ~ 1.8 teraannus years 

########section III 

19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11

## using the context, I'm going assume, there will be attack in it

# A T T A == 19 17 17 19 

19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11

A  T  T  A  C  K  23 18 19 "8" 12 16 19 "8" 3 21 "8" 25 18 14 18 6 3 18 8 15 18 22 18 11

# as messages were rarely large messages as more letters meant easier to encrypt and were more expensive time wise to get and write it could be assumed that right after attack there would be the place
# pearl harbor has 3 R's in it pos 4, 7, 9

19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11
A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R 25 18 14 18 6 3 18 8 15 18 22 18 11


# this final part if it is ATTACKPEARLHARBOR, is probably a date, and maybe a number, there isn't enough letters left for any number bigger then 12 (thirteen vs twelve, eleven, ten)
# so it is probably a date numb 
# Pearl harbor was probably highphenated in the original message, so the japense probably did not shift the letters on the new word, this can be seen on the A's in Pearl Harbor vs Attack
# it seems that the data - numb is together as well, they share the same shift 


A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R 25 "18" 14 "18" 6 3 "18" 8 15 "18" 22 "18" 11
only one month has that manY of one character in that kind of order DECEMBER 

A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R 25 18 14 18 6 3 18 8 15 18 22 18 11
A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R D  E  C  E  M B E  R 15 E  22 E  11

being that DECEMBER fat nicely in there it can be assumed that that the 2 ending 18's are E, as such 7 fits well in there

A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R D  E  C  E  M B E  R S E  V E  N

ATTACKPEARLHARBORDECEMBERSEVEN 











"""




        