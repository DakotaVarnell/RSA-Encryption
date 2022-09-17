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


    



#Create our list of possible candidate prime numbers
candidates = create_candidates()

#Assign our return variables to p and q as they should be
p, q = fermats_theorum(candidates)
print(p, q)
print("Test Dakota12")

