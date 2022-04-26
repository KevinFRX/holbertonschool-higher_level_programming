#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print(f"Last digit of {number} is", end=' ')

if number < 0 and abs(number) % 10 != 0:
    print("-", end='')

print(abs(number) % 10, "and is", end=' ')

if number < 0 and abs(number) % 10 != 0 or abs(number) % 10 < 6:
    print("less than 6 and not 0")
elif int(repr(number)[-1]) > 5:
    print("greater than 5")
else:
    print("0")
