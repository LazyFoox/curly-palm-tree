# importing Pip
import random
from random import randint


# random text

T1 = [
    "Hello",
    "Testing",
    "Haaaaaaa",
] # getting some text in there
print(random.choice(T1)) # randomized picking from the get text

# Random integers

T2 = randint(0,255) # Getting a randomize number
print(T2) #printing the finished random number

# password

text = "abcdefghijklmnopqrstuvwxyz"
TEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
special = "@#$&-+_\/*"

mix = text + TEXT + num + special
length = 8

final = "".join(random.sample(mix, length)) #random.sample is a scrambled random words
print(final)
