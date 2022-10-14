from random import randint
from random import shuffle
from random import choice
  # random
 # Python comes with a built in random library. There are a lot of functions included in this 
 #random library, so we will only 
  #show you two useful functions for now.
print("random")
dice1 = randint(1,7)
print(f"dice1 : {dice1}")
dice2 = randint(1,7)
print(f"dice2 : {dice2}")
rolledDoubles = dice1 == dice2
if rolledDoubles:
  print("you rolled doubles")
else: print("not doubles")

# create a way to roll snakes
if dice1 and dice2 ==1:
  print("you rolled snake eyes")
else: print("you did not roll snake eyes")

# practice with shuffle
my_list = range(1,51)
print("my new list")
print(list(my_list))
my_list = list(my_list)
shuffle(my_list)
print(my_list)

random = randint(1,201)
print(random)

if (random % 2) == 0:
  print("{0} is Even number". format(random))
else:
  print("{0} is Odd number". format(random))

color = ["red", "blue", "pink", "purple"]
random_color = choice(color)
print(f"random color is {random_color}")

  # Random Practice #1
  # Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.
random_number = randint(1,11)
print(f"random_number : {random_number}")
  
  # Random Practice #2
  # Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.
random_number = randint(0,2)
print(f"random_number : {random_number}")
  
  # Random Practice #3
  # Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.
  
names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
raffle = choice(names)
print(f"random winner is {raffle}")
  
  