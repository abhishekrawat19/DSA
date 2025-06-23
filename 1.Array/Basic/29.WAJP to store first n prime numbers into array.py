# WAJP to store first n prime numbers into array.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def store_first_n_primes(n):
    primes = []
    num = 2  # Start checking from 2

    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes

# Example: Get first 5 prime numbers
print(store_first_n_primes(5))
