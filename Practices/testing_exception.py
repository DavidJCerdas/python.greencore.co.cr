def testing_exception(value):
    if value == 1:
        return "yes, value is 1"
    raise Exception("the value is not 1")

try:
    testing_excetion(2)
except Exceptionn:
    print('It has an exception')
print('But this program continues though the exception')