#!/usr/bin/env python3

"""
The following hex strings were pulled from the program via reverse engineering
0x48426a50434a7a77 (wzJCPjBH)
0x6162486b41487342 (BsHAkHba)
0x7a6c666459686d7a (zmhYdflz)
0x455550706168644c (LdhapPUE)

Supposedly these are the portions that make up the password
"""
import string
import random
import subprocess

passw = "wzJCPjBHBsHAkHbazmhYdflzLdhapPUE" # found within the program

user_in = "test"

def val(comp, app):

    count = 0
    i = 0

    while i < comp:
        count += ord(app[i])
        i += 1
  
    return count

#print(val(len(user_in), user_in))

valid_chars = string.ascii_letters + string.digits

def key_gen():
    temp = []

    # generating random base key
    while len(temp) < 32:
        gen = random.choice(valid_chars) 

        # ensures the key is not invalid
        while gen in string.punctuation:
            gen = random.choice(valid_chars) 

        temp.append(gen)


  
    while (v := val(len(temp), "".join(temp))) < 2977:
        #print(v)

        # select a random element from the array and add one
        r = random.randrange(0, len(temp))
        gen = chr(ord(temp[r]) + 1)
        while gen in string.punctuation:
            gen = random.choice(valid_chars) 

        temp[r] = gen

    # check if greater than, and restart

    while val(len(temp), "".join(temp)) > 2977:
        print("Attempting to generate another key...")

        # remove the difference from random element to get a valid key
        offset = val(len(temp), "".join(temp)) - 2977 # e.g 13
        try:
            for i in range(0, len(temp)):
                x = chr(ord(temp[i]) - offset)
                
                if x not in string.punctuation:
                    temp[i] = x
                    break
        except Exception as e:
            key_gen()
            break
        #return "f" * 32

    return "".join(temp)


#key = key_gen()
#print(key)
#print("Stats: len {0} - size {1}".format(len(key), val(len(key), key)))

for i in range(1):
    generated_string = key_gen()

    while val(len(generated_string), generated_string) != 2977:
        generated_string = key_gen()

    print("Key: {0}".format(generated_string))
    
    subprocess.call(["/home/kali/Desktop/Projects/_Studies/ReverseEngineering/crackmes_org/SilentWraith_lockcode/lockcode",generated_string])
    print()
