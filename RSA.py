import random
import math

def create_candidates(n = 1000000):
    candidates = []
    x = 0
    for i in range(100):
        x = random.randint(n, n * 10)
        if x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 != 0 and x%11 != 0:
            candidates.append(x)
    return candidates

def fermats_theorem(candidates = []):
    primes = []
    n = 10

    while len(primes) < n:
        for i in candidates:
            for k in range(20): #performs Fermat's test 20 times
                a = random.randint(2, i//2) #Find an 'a' to perform Fermat's Theorem
                while math.gcd(a, i) != 1: #if gcd is not one, the 'a' and 'i' are not relatively prime
                    a = random.randint(2, i//2)
                if pow(a , i - 1, i) == 1: #if the number passes Fermat's Test then add it to primes
                    primes.append(i)
                break

    p = primes[0]
    q = primes[1]
    return(p, q)

#the requirements for e are that it must be less than phi and it must be relatively prime to phi
def generate_e(phi):
        for i in range(1):
            x = random.randint(2, phi-1)
            if math.gcd(x, phi) == 1: #if e and phi are relatively prime, they're gcd must be 1
                e_ = x
            else:
                continue

        return e_

#M is the message (in ASCII) to encrypt
#N and e are the public key
def encrypt(M, e, N):
    encryted_message = []
    for i in M:
        encryted_message.append(pow(i, e, N))

    return encryted_message
        

#this takes each individual character and finds its ASCII correspondence
#it then adds it to the list message_in_ascii
def message_to_ascii(message_in_char):
    message_in_ascii = []
    message_in_char = message_in_char.upper()
    for i in message_in_char:
        message_in_ascii.append(ord(i))

    return message_in_ascii

    



#Create our list of possible candidate prime numbers
candidates = create_candidates()

#Assign our return variables to p and q as they should be
p, q = fermats_theorem(candidates)
print('The value of p is: ', p, 'The value of q is: ', q)

N = p*q
phi = (p-1)*(q-1)

e = generate_e(phi)
print('e is:', e)

public_key = [N, e]

h = message_to_ascii('Hello')
print(h)
print(encrypt(h, e, N))
