# The idea is to understand loops can ended up with else statement
for i in range(3):
  print(i)
else:
  print('At this point for ends and i has a value of:{0}'.format(i))

i = 0
while i < 3:
  print(i)
  i += 1
else:
  print('At this point while ends and i has a value of:{0}'.format(i))
