"""
    Counting the amount of times each letter appears in a sentence, and use pprint to display the result
"""
import pprint

message = "Costa Rica is Pura Vida."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
