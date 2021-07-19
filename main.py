"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

number = 600851475143
factors = []

for i in range(2, round(sqrt(number))):
    if number % i == 0:
        number /= i
        factors.append(i)

print(f'Largest prime factor of number 600851475143 is {factors[-1]}')
