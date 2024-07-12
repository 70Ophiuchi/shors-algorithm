import math
import os
from termcolor import colored
from time import sleep
from tqdm import tqdm
from art import *

os.system("color")

# p . q = mN
# g^p = mN + 1
# g^p - 1 = mN

# g = 8
# N = 77

# print("STARTING PROGRAM")
# for i in tqdm(range(10)):
#     sleep(0.5)

loading_time = 0.1

tprint("Shor's   Algorithm", font="tarty1")

def find(g, N):
    
    for x in range(1, 100):
        if math.pow(g, x)%N == 1:
            # print(int(math.pow(g,x)), prime)
            return x
        else:
            continue
    return "No value found"

# print(find(77))

# (g^(p/2) - 1) (g^(p/2) + 1) = mN
# mN = p . q

def solve(g, p):
    small_p = p/2
    big_g = int(math.pow(g, small_p))
    big_g_minus_one = big_g - 1
    big_g_plus_one = big_g + 1
    
    # print(big_g_minus_one, big_g_plus_one)
    return (big_g_minus_one, big_g_plus_one)
    
def euclid(a, N):
    
    if a%N == 0:
        # print(N)
        return N
    
    dividend = a
    divisor = N
    remainder = dividend%divisor
    return euclid(divisor, remainder)

# s_1, s_2 = solve(find(N))

# p = euclid(s_1, N)
# q = euclid(s_2, N)

def crack():
    
    N = -1
    g = -1

    while int(N) <= 0:
        try: 
            N = int(input(colored("\nEnter Number (Positive Integer): ", "light_blue")))
            if N > 0:
                break
            else:
                print(colored("\nInvalid Number", "light_red"))

        except Exception as e:
            print(colored("\nInvalid Number", "light_red"))

    while int(g) <= 0:
        try:
            g = int(input(colored("Enter Guess (Positive Integer less than Number): ", "light_blue")))
            if g > 0:
                break
            else:
                print(colored("\nInvalid Number", "light_red"))

        except Exception as e:
            print(colored("\nInvalid Number", "light_red"))

    
    print("")
    sleep(0.5)
    print(colored("-"*32, "yellow"))
    print(colored("\nFORMULAS: \n", "green"))
    print(colored("g^p = mN + 1", "magenta"))
    print(colored("p . q = mN", "magenta"))
    print(colored("(g^(p/2) - 1) (g^(p/2) + 1) = mN", "magenta"))
    print(colored("(g^(p/2) - 1) (g^(p/2) + 1) = p . q\n", "magenta"))
    print(colored("-"*32, "yellow"))
    sleep(2)    
    
    print(colored("\nFinding p...\n", "blue"))
    p = find(g, N)
    for i in tqdm(range(10), colour="blue"):
        sleep(loading_time)
    print(colored("\np: {}\n".format(p), "red", attrs=["bold"]))
    
    print(colored("-"*32, "yellow"))
    
    try:
        print(colored("\nSolving for {}^({}/2) + 1 and {}^({}/2) - 1...\n".format(g, p/2, g, p/2), "blue"))
    except Exception as e:
        print(colored("\nAlgorithm failed, no suitable p value found\n", "yellow"))
        exit()
    a_1, a_2 = solve(g, p)
    for i in tqdm(range(10), colour="blue"):
        sleep(loading_time)
    print(colored("\n{}^{} - 1: {} (a_1)\n{}^{} + 1: {} (a_2)\n".format(g, p/2, a_1, g, p/2, a_2), "red", attrs=["bold"]))
    
    print(colored("-"*32, "yellow"))
    
    print(colored("\nFinding GCD for a_1 and Number using Euclid's Algorithm...\n", "blue"))
    p = euclid(a_1, N)
    for i in tqdm(range(10), colour="blue"):
        sleep(loading_time)
    print(colored("\nGCD(a_1, {}): {}\n".format(N, p), "red", attrs=["bold"]))
    
    print(colored("-"*32, "yellow"))
    
    print(colored("\nFinding GCD for a_2 and Number using Euclid's Algorithm...\n", "blue"))
    q = euclid(a_2, N)
    for i in tqdm(range(10), colour="blue"):
        sleep(loading_time)
    print(colored("\nGCD(a_2, {}): {}\n".format(N, q), "red", attrs=["bold"]))
    
    print(colored("-"*32, "yellow"))
    
    print(colored("\nMultiplying p and q to verify result...\n", "blue"))
    for i in tqdm(range(10), colour="blue"):
        sleep(loading_time)
    print(colored("\nN: {}\np: {}\nq: {}\n\n{} x {} = {}\n\nCracked = {}\n".format(N, p, q, p, q, p*q, (p*q == N)), "red", attrs=["bold"]))

if __name__ == "__main__":
    crack()
