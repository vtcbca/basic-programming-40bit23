def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit) if primes[p]]

def is_prime_sieve(n, primes):
    return n in primes

# Example usage:
limit = 1000  # Change as needed
primes = sieve_of_eratosthenes(limit)
print(is_prime_sieve(11, primes))