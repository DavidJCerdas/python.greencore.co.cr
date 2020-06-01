"""
    Counting the amount of times each letter appears in a sentence.
"""

message = "Costa Rica is Pura Vida"
count = {}

for character in message:
    count.setdefault(character, 0)
    print("count[{0}] {1} and count[{0}] + 1:{2}".format(character, count[character], count[character]+1))
    count[character] = count[character] + 1

print("count: {0}".format(count))
