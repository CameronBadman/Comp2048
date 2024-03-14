code = "19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11"


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

assuming the characters are the same for the whole message

A  T  T  A  C  K  23 18 A "8" 12 16 19 "8" 3 21 "8" 25 18 14 18 6 3 18 8 15 18 22 18 11

# as messages were rarely large messages as more letters meant easier to encrypt and were more expensive time wise to get and write it could be assumed that right after attack there would be the place
# pearl harbor has 3 R's in it pos 4, 7, 9

19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11
A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R 25 18 14 18 6 3 18 8 15 18 22 18 11

assuming the characters are the same for the whole message

19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11
A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R 25 E  14 E  6 3 E  R 15 E  22 E  11


# this final part if it is ATTACKPEARLHARBOR, is probably a date, and maybe a number, there isn't enough letters left for any number bigger then 12 (thirteen vs twelve, eleven, ten)
# so it is probably a date numb 

A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R 25 "18" 14 "18" 6 3 "18" 8 15 "18" 22 "18" 11
only one month has  that many e's, DECEMBER 

A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R 25 18 14 18 6 3 18 8 15 18 22 18 11
A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R D  E  C  E  M B E  R 15 E  22 E  11


A  T  T  A  C  K  P  E  A  R L  H  A  R B O  R D  E  C  E  M B E  R S E  V E  N

ATTACKPEARLHARBORDECEMBERSEVEN 











"""




        