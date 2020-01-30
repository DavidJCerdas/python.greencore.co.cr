#!/usr/bin/python3
# This software shows some common exceptions and its handling, this for the next MeetUp
import os

# Division by 0
def zero_division_test():
    for i in reversed(range(5)):
        try:
            result = 10 / i
        except ZeroDivisionError:
            print("ZeroDivisionError: Be careful, it is not possible to divide 10 by 0.")
        else:
            print("Lets divide: 10/{0} = {1}".format(i, result))
        finally:
            print("We are done with {0}".format(i))
            print("-------------------------------------------------------------------------------")
    print("This program is done.")

# raise an exception with specific parameters.
def raise_customized_e():
    try:
        print("# apt install python10")
        raise Exception(1, 'Python 10 has not yet been released.')
    except Exception as custom_exception:
        # type of custom_exception
        print(type(custom_exception))
        # Arguments in custom_exception
        print(custom_exception)
        # Let's get the arguments back.
        print("{0}: {1}".format(os.strerror(custom_exception.args[0]), custom_exception.args[1]))


# Testing Exceptions
# zero_division_test()
# raise_customized_e()
