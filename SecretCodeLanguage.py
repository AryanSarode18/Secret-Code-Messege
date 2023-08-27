# Importing random and string
import random, string

# Welcome Script
print("Welcome To Secret Code Language App")

# Generating 3 random characters
r1 = random.choice(string.ascii_letters)
r2 = random.choice(string.ascii_letters)
r3 = random.choice(string.ascii_letters)

# Coding The Word To Scret Language
def code():
    a = input("Enter the word to get changed in secret language : ")
    if len(a) <= 2:
        new = a[::-1]
        print(new)
    else:
        n1 = a[1:]+a[0]
        new = r1+r2+r3+n1
        print(new)

# Decoding The Word From Scret Language To Normal
def decode():
    a = input("Enter the word to get decoded : ")
    if len(a) <= 2:
        new = a[::-1]
        print(new)
    else:
        new = a[-1]+a[3:-1]
        print(new)

# Asking whether to code or decode
a = input("Do You Want To Code Or Decode (C/D) : ")
if a == "C" or a == "c":
    code()
elif a == "D" or a == "d":
    decode()
else:
    print("Enter a Valid Input")
    exit()