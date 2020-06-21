#!/usr/bin/python
# This software generates random numbers between 0 to 10, and repeat the sum n amount of times
example='''
root@djcerdasjupyter-VirtualBox:~# ./recursion_practice1.py 3
Starting the sum...
This is the final sum:10, after sum the list of random numbers:
[5, 3, 2]
root@djcerdasjupyter-VirtualBox:~# ./recursion_practice1.py 3
Starting the sum...
This is the final sum:9, after sum the list of random numbers:
[2, 5, 2]
'''
import random
from random import seed
from datetime import datetime
import sys

# Amount of times to repeat
interactions = sys.argv[1]

def sum(repeat=0, sum_number=0, numbers=[]):
    # generate a new random number to sum
    random.seed(datetime.now())
    number = random.randrange(1, 10)
    numbers.append(number)
    sum_number = sum_number + number
    repeat = int(repeat) - 1
    if repeat == 0:
        # print the random numbers in the list
        print("This is the final sum:{0}, after sum the list of random numbers:\n{1}".format(int(sum_number), numbers))
        return 0
    sum(int(repeat), sum_number, numbers)

if __name__ == '__main__':
    print("Starting the sum...")
    sum(interactions)
