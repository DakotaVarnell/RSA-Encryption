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


def fermats_theorum(candidates = []):
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

#creates N
def createN(p,q):
    n = p *q
    return n

#creates what Phi would be
def createPhi(p,q):
    phi = (p -1)*(q-1) 
    return phi

#Euclid's algorithm for finding gcd
def eagcd(a, b):
    if b == 0:
        return a
    else:
        return eagcd(b, a % b)

#Euclid's extended algorithm that uses mod inverse
def eeagcd(a, b):
    if a ==0:
        return (b, 0, 1)
        (g, x1, y1) = eeagcd(b % a, a)
        x = y1 - (b//a) * x1
        y = x1

        return g,x,y

#Mod inverse
def modular_inverse(a,b):
    g,x,y = eeagcd(a,b)
    if g != 1:
        raise Exception("No modular inverse")
    else: 
        return x % b    



#Create our list of possible candidate prime numbers
candidates = create_candidates()

#Assign our return variables to p and q as they should be
p, q = fermats_theorum(candidates)
print(p, q)
n = createN(p,q)
phi = createPhi(p,q)
print("Test")

