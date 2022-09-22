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
def generate_e(phi_):
    list_of_e = [] #a list of possible values for e
    while len(list_of_e) < 1:
        for i in range(20): #20 chances at finding phi - we can change this to find only one value later on
            x = random.randint(2, phi-1)
            if math.gcd(x, phi) == 1: #if e and phi are relatively prime, they're gcd must be 1
                list_of_e.append(x)
            else:
                continue

    return list_of_e

# def print_options():
#     print("RSA Keys Have Been Generated.")
#     print("Please Select Your User Type:")
#     print("\t1. A public user")
#     print("\t2. The owner of the keys")
#     print("\t3. Exit program")
#     print("Enter Your Choice: ", end = '')


# def choose_option():
#     a = True
#     while(a):
#         print("RSA Keys Have Been Generated.")
#         print("Please Select Your User Type:")
#         print("\t1. A public user")
#         print("\t2. The owner of the keys")
#         print("\t3. Exit program")
#         print("Enter Your Choice: ", end = '')

#         choice = int(input())

#         match choice:
#             case 1:
#                 choice_case_1= int(input())
#                 print("As a public user, what would you like to do?")
#                 print("\t1. Send an encrypted message " )
#                 print("\t2. Authenticate a digital signature ")
#                 print("\t3. Exit")

#                 match choice_case_1:
#                     case 1:
#                         a = False
#                         return(input("Enter a message: "))
#                     case 2:

#                     case 3:


#             case 2:
#                 return "two"
#             case 3:
#                 return "three"
#             case default:
#                 return "something"
 
    

#M is the message to encrypt
#N and e are the public key
def encrypt(M, N, e):
    return pow(M, e, N)

    



#Create our list of possible candidate prime numbers
candidates = create_candidates()

#Assign our return variables to p and q as they should be

p, q = fermats_theorem(candidates)

N = p*q
phi = (p-1)*(q-1)

e = generate_e(phi)

public_key = [N, e]

#Our frontend begins here
a = True
encryption_list = []
signature_list = []
signature_validity = True

while(a):
    print("RSA Keys Have Been Generated.")
    print("Please Select Your User Type:")
    print("\t1. A public user")
    print("\t2. The owner of the keys")
    print("\t3. Exit program")
    print("Enter Your Choice: ", end = '')

    choice = int(input())

    match choice:
        case 1:
            print("As a public user, what would you like to do?")
            print("\t1. Send an encrypted message " )
            print("\t2. Authenticate a digital signature ")
            print("\t3. Exit")
            print("Choose One: ", end = "")
            choice_case_1= int(input())

            b = True
            
            while(b):
                    match choice_case_1:
                        case 1:
                            a = False
                            our_string = (input("Enter a message: "))
                            #this is where our conversion function needs to be called
                            #this is where our encryption function needs to be called on our converted string
                            print("Message encrypted and sent")
                            b = False
                        case 2:
                            if len(signature_list) == 0:
                                print("There are no signatures to authenticate.")
                            else:
                                print("The following messages are available: ")
                                for i in range(len(signature_list)):
                                    print(i + ". " + signature_list[i])
                                    choose_message = int(input())
                                    
                                    if signature_validity == True:
                                        print("Signature is valid.")
                                    else:
                                        print("Signature is not valid")
                            b = False
                        case 3:
                            b = False
        case 2:
            print("As the owner of the keys, what would you like to do?")
            print("\t1. Decrypt a received message " )
            print("\t2. Digitally sign a message ")
            print("\t3. Exit")
            print("Choose One: ", end = "")
            choice_case_2 = int(input())

            c = True
            
            while(c):
                    match choice_case_2:
                        case 1:
                            print("The following messages are available")

                            for i in range(len(encryption_list)):
                                print(i + ". " + "length = " + len(encryption_list[i]))
                                choose_message = int(input())

                            for i in range(len(encryption_list)):
                                if choose_message == i:
                                    #decrypt the message at encryption_list[i]
                                    print("Decrypted Message: " + "decrypted_message")
                                    c = False
                        case 2:
                            message = input("Enter a message: ")
                            #sign our message and send it
                            c = False
                        case 3:
                            c = False
        case 3:
            print("Bye for Now!")

