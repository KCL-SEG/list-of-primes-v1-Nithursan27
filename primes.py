"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 2
    count = 0
    while(len(list) < number_of_primes):
        isPrime = True
        i = 1
        while(isPrime and i < number):
            if(number % i == 0 and i != 1):
                isPrime = False
            i += 1
        if(isPrime):
            list.append(number)
        number += 1
    return list
