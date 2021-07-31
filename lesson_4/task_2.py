
# Sieve of Erathosthenes
# to find i-th prime number, maximum n = 100000

n_max = 10000
def SieveOfEratosthenes_i(i):
    """At first implements the whole algorithm and then finds ith element out of it"""
    # list of all numbers
    all_numbers = list(range(2, n_max+1))
    j = 0
    while j < n_max:
        c_n = all_numbers[j]
        # start from that number and step is the same number
        # zero out all numbers divisible on that number
        for n in range(j+c_n, n_max-1, c_n):
            if all_numbers[n] == 0:
                continue
            else:
                all_numbers[n] = 0
        # to break out of while if sum of all next numbers is 0
        if sum(all_numbers[j+1:]) == 0:
            break
        # find index of the next non-zero number
        for c_j in range(j+1, n_max-1):
            if all_numbers[c_j] != 0:
                j = c_j
                break
    # to find prime numbers
    primes = []
    for n in all_numbers:
        if n != 0:
            primes.append(n)
    return primes[i-1]


def SieveOfEratosthenes_improved_i(i):
    """Does not implement the whole algorithm but only up to i"""
    # starting from 2
    primes = [2]
    # list of all numbers
    all_numbers = list(range(2, n_max+1))
    j = 0
    while i > len(primes) and j < n_max:
        c_n = all_numbers[j]
        # start from that number and step is the same number
        # zero out all numbers divisible on that number
        for n in range(j+c_n, n_max-1, c_n):
            if all_numbers[n] == 0:
                continue
            else:
                all_numbers[n] = 0
        # find index of the next non-zero number
        # to break out of while if sum of all next numbers is 0
        if sum(all_numbers[j+1:]) == 0:
            break
        for c_j in range(j+1, n_max-1):
            if all_numbers[c_j] != 0:
                j = c_j
                break
        primes.append(all_numbers[j])
    return primes[i-1]


# to measure execution time
from timeit import timeit

def init_function(func_name):
    return f"""
from __main__ import {func_name}
i = 50
"""


print('Finding i-th prime number with the sieve of Erathosthenes time is ', round(timeit(setup=init_function('SieveOfEratosthenes_i'),
             stmt="SieveOfEratosthenes_i(i)",
             number=10000), 2), ' usecs')
print('Finding i-th prime number where limit to sieve was added as well as filling list of primes gradually is ',
      round(timeit(setup=init_function('SieveOfEratosthenes_improved_i'),
             stmt="SieveOfEratosthenes_improved_i(i)",
             number=10000), 2), ' usecs')

"""As the result of time mesurement for input number of 50 out of 10000 numbers the timing of:
    - the improved algorithm of finding an i-th prime number is about 10 times faster comparing to the full one
"""

# profiling the execution
import cProfile

def main():
    i = 50
    prime_i = SieveOfEratosthenes_i(i)
    prime_improved_i = SieveOfEratosthenes_improved_i(i)

cProfile.run('main()')

"""cProfile gave similar results to timeit"""



