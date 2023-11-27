import random

randomnumber = random.randint(0,10)
chances = 5

print("Guess the random number between 1 and 10")
while chances <= 5:
  guess = int(input("Enter your guess: "))
  if(guess < randomnumber):
    print("Your guess is too low!")
  if(guess > randomnumber):
    print("Your guess is too high")
  if guess == randomnumber:
    print("You got it!")
    break
  chances = chances - 1

if chances == 0:
  print("You lose! the number is ", randomnumber)
  