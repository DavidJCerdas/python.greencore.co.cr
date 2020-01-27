#!/usr/bin/python
# This software shows some common exceptions and its handling.

# Division by 0
def ZeroDivisionError_test():
    for i in reversed(range(5)):
        try:
            print("Lets divide: 10/{0} = {1}".format(i,10/i))
        except ZeroDivisionError:
            print("ZeroDivisionError catched: Be careful, it is not possible to divide by 0")
    print("done!")

# Testing Exceptions
ZeroDivisionError_test
       
