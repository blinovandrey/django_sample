print('Hello, Django girls!')
if 1 > 3:
  print('no')
elif 5 > 2:
  print ('five > two')
else:
  print('yes')

def my(arg):
  if arg > 17:
    print (str(arg) + 'bigger')
  else:
    print (str(arg) + 'smaller')

numbers = [1, 14, 18, 20]

for num in numbers:
  my(num)
  print ("next num")

for i in range(1, 19):
  my(i)