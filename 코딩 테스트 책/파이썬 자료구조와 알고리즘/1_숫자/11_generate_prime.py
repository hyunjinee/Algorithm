import math
import random
import sys

def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4:
        return True
    for x in range(2, int(math.sqrt(num))+1):
        if number  % x == 0:
            return False
    return True


def generate_prime(number =3):
    while 1:
        p = random.randint(pow(2, number-2), pow(2, number-1)-1)
        p = 2* p +1
        if finding_prime_sqrt(p):
            return p



if __name__ == "__main__":
   
    if len(sys.argv) < 2:
        print("Usage: generate_prime.py number")
        sys.exit()
    else:
        number = int(sys.argv[1])
        print(generate_prime(number))
    
