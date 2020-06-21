# In this example continue is going to go back to the for, skipping 2 and 4 for being printed
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)