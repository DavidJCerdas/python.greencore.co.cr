"""
    Just a routine practice: The idea is to create 3 functions to uppercase
     the first and fourth letter of a word.
"""
word = "macdonald"


def cap_word1(word, i=0):
    for letter in word:
        if i == 0 or i == 3:
            word = word.replace(letter, letter.upper(), 1)
        i = i + 1
    return word


def cap_word2(word):
    list_x = list(word)
    list_x[0] = list_x[0].upper()
    list_x[3] = list_x[3].upper()
    return ''.join(list_x)


def cap_word3(word):
    first_letter = word[:3]
    second_letter = word[3:]
    return first_letter.capitalize() + second_letter.capitalize()


print("Result: {0}".format(cap_word1(word)))
print("Result: {0}".format(cap_word2(word)))
print("Result: {0}".format(cap_word3(word)))
