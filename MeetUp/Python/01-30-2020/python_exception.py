#!/usr/bin/python
# This software shows some common exceptions and its handling, this for the next MeetUp

# Division by 0
def zero_division_test():
    for i in reversed(range(5)):
        try:
            print("Lets divide: 10/{0} = {1}".format(i, 10 / i))
        except ZeroDivisionError:
            print("ZeroDivisionError catched: Be careful, it is not possible to divide 10 by 0.")
    print("Done!")

# FileNotFoundError
def file_not_found_test():
    try:
        f_d = open("dog_names.txt", "r+")
        print("Printing names:\n"+f_d.read())
        # Close opened file
        f_d.close()
    # Lets get the exception object <exceptions.ZeroDivisionError instance>"
    except FileNotFoundError as my_exception:
        print(type(my_exception))
        print(my_exception)


# Testing Exceptions
# zero_division_test()
# file_not_found_test()
