import random

def guess(x):
  random_number = random.randint(1,x)
  guess = 0 
  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
      print('Sorry, The number is too low. Try Again.')
    elif guess > random_number:
      print('Sorry, The number is too big. Please try again.') 

  print(f'Congratulations! You have guessed the number {random_number}')

def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input(f'Is {guess} too low (L), too high (H) or correct (C)')
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1 

print(f'Yay! The computer guessed your number, {guess}, correctly!')

guess(10)