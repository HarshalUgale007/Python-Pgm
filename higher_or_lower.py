#higher or lower

import random as ran

def decorator(func):

  def wrapper(*a, **ar):
    print("*.*.*.*.*.*.*.*.*")
    func(*a, **ar)
    print("*.*.*.*.*.*.*.*.*")

  return wrapper

@decorator
def higher_or_lower():
  print("Welcome to Higher or Lower!")
  print("I'm thinking of a number between 1 and 50.")
  print("Can you guess what it is?")
  print("You have 10 tries to guess the number.")
  print("Let's begin!")

  number = ran.randint(1, 50)

  tries = 10

  while tries > 0:
    print("You have", tries, "tries left.")
    guess = int(input("Enter your guess: "))

    if guess == number:
      print("Congratulations! You guessed the number!")
      return

    elif guess < number:
      print("Your guess is too low. Try again.")

    else:
      print("Your guess is too high. Try again.")

    tries -= 1

  print("Sorry, you ran out of tries. The number was", number)


print(higher_or_lower())
