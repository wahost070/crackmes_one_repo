#!/usr/bin/env python3

"""
@author wahost070
@date 26.01.21
"""

import random, string, subprocess

valid_chars = string.ascii_letters + string.digits

def check_serial(key):
    step = 0
    while step < 0x10: #16
        if ord(key[step]) - ord(key[step + 1]) == -1:
            step += 2
        else:
            return 1
        return 0
    else:
        return 1


def gen_key():
    my_key = []

    for x in range(0, 16, 2):
        try:
            val = ord(random.choice(valid_chars))

            # if there are symbols in the generated values, then regenerate by generating a new value
            while chr(val) in string.punctuation or chr(val + 1) in string.punctuation:
                val = ord(random.choice(valid_chars))

            my_key.append(chr(val))
            my_key.append(chr(val + 1))
        except Exception as e:
            print("There was an exception: {0}".format(e))
            print("Attempting to generate another key...")
            gen_key()
            break
    return ''.join(my_key)

for i in range(5):
    generated_string = gen_key()

    while check_serial(generated_string) != 0:
        generated_string = gen_key()

    print("Key: {0}".format(generated_string))
    
    subprocess.call(["./unedit/SimpleKeyGen",generated_string])
    print()
