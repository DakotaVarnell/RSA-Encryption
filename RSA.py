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
    e_is_empty = True
    while(e_is_empty):
        x = random.randint(2, phi-1) #e must be in the range of phi
        if math.gcd(x, phi) == 1: #if e and phi are relatively prime, they're gcd must be 1
            e_ = x
            e_is_empty = False
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

#Euclid's algorithm for finding gcd
def eagcd(a, b):
    if b == 0:
        return a
    else:
        return eagcd(b, a % b)

#Euclid's extended algorithm that uses mod inverse
def eeagcd(a, b):
    if a == 0:
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

#Uses eagcd to create a public key
def create_public_key(phi):
    e = random.randint(2,phi)
    i = eagcd(phi,e)
    while i != 1:
        e = random.randint(2,phi)
        i = eagcd(phi, e)
    return e

#uses eeagcd to create the private key
def create_Private_Key(phi,e):
    d = modular_inverse(e,phi)
    return d

#Simply display a prompt for user input of the message portion of signature
def getString():
    Sinput = input("Please type in a string: ")
    return Sinput

#Will create the signature using the input message and private key
def creat_signature(Sinput, d, n):
    Sinput_in_ascii = (Sinput) #<-- parenthesis is a placeholder, delete when uncomment --> #Sinput_in_numeric(Sinput)
    signed = pow(Sinput_in_ascii,d,n)
    return signed

#Authenticates the digital signature 
def authenticate_signature(signature, n, e, Sinput_in_ascii):
    message = pow(signature, e, n)
    if message == Sinput_in_ascii:
        return True
    else:
        return False



#Create our list of possible candidate prime numbers
candidates = create_candidates()

#Assign our return variables to p and q as they should be
p, q = fermats_theorem(candidates)

#Create our N
N = p*q

#Create our phi
phi = (p-1)*(q-1)

#Create our e
e = generate_e(phi)

#Generate our public keys
public_key = [N, e]

#Generate d
d = create_Private_Key(phi, e)

#Our frontend begins here
a = True
encryption_list = []
signature_list = []
signature_validity = True
print("RSA Keys Have Been Generated.")

while(a):
    print("\nPlease Select Your User Type:")
    print("\t1. A public user")
    print("\t2. The owner of the keys")
    print("\t3. Exit program")
    print("Enter Your Choice: ", end = '')

    choice = int(input())

    match choice:
        case 1:
            b = True
            
            while(b):
                
                print("\nAs a public user, what would you like to do?")
                print("\t1. Send an encrypted message " )
                print("\t2. Authenticate a digital signature ")
                print("\t3. Exit")
                print("Choose One: ", end = "")
                choice_case_1 = int(input())


                match choice_case_1:
                        case 1:
                            our_string = (input("Enter a message: "))
                            message_to_encrypt = message_to_ascii(our_string) #the inputted string is transformed to ASCII 
                            encryption_list.append(encrypt(message_to_encrypt,e,N)) #message encrypted
                            print("Message encrypted and sent")
                        case 2:
                            if len(signature_list) == 0:
                                print("There are no signatures to authenticate.")
                            else:
                                print("The following messages are available: ")
                                for i in range(len(signature_list)):
                                    print(str(i + 1) + ". " + signature_list[i])
                                print("Choose One: ", end = "")
                                choose_message = int(input())
                                    
                                if signature_validity == True:
                                    print("Signature is valid.")
                                else:
                                    print("Signature is not valid")
                        case 3:
                            b = False
        case 2:

            c = True
            
            while(c):
                print("\nAs the owner of the keys, what would you like to do?")
                print("\t1. Decrypt a received message " )
                print("\t2. Digitally sign a message ")
                print("\t3. Exit")
                print("Choose One: ", end = "")
                choice_case_2 = int(input())
                    
                match choice_case_2:
                    case 1:
                        print("\nThe following messages are available")

                        for i in range(len(encryption_list)):
                            print(str(i + 1) + ". " + "length = " + str(len(encryption_list[i])))
                        
                        print("Choose One: ", end = "")
                        choose_message = int(input())

                        for i in range(len(encryption_list)):
                            if choose_message == i + 1:
                                #decrypt the message at encryption_list[i]
                                print("Decrypted Message: " + "decrypted_message")
                    case 2:
                        message = input("Enter a message: ")
                        message = message_to_ascii(message)
                        signature_list.append(int(creat_signature(message, d, N)))
                        print("Message signed and sent")
                    case 3:
                        c = False
        case 3:
            print("Bye for Now!")
            a = False

