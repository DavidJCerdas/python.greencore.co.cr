# Simple script to request a name and make some error control
ERROR1 = "the name has spaces, please put only a name."
ERROR2 = "only the first letter needs to be in uppercase."
ERRORS = [0,ERROR1, ERROR2]

def alrevez(string_word):
    word = list(string_word)
    word.reverse()
    return "".join(word)

def control_errores(string_word):
    if " " in name:
        return 1
    if name != name.capitalize():
        return 2
    return 0

name = input("Hi, please write your name?: ")

print_x = control_errores(name)
if print_x == 0:
    print("Hello, {0}".format(alrevez(name).capitalize()))
if print_x > 0:
    print("Error: the name entered does not have the right format, {0}".format(ERRORS[print_x]))
