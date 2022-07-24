import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")

#while loop to count the number of chances
while chances < 5:
   guessNumber = int(input("enter your guess number:"))

#comparing the user entered number with the number to be guessed
   if guessNumber == number:
      print("CONGRATULATION, YOU WON!!!")
      break

   elif guessNumber < number:
      print("Your guess was too low, guess a nummber higher than", guessNumber)

   else:
      print("Your guess was too high, guess a number lower than", guessNumber)

   chances +=1

#check weather the user guessed the correct no.

if not chances < 5:
   print("YOU LOSE..!, The number is", number)







