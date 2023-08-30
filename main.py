import random
secretnum = random.randint(0,5)
count = 1

while(True):
    guess = int(input("Guess the num bw 0-50. "))
    if guess == secretnum:
     print("hurray you guessed it correct.")
     break
    else:
     print("try again")
     count = count + 1
     if count > 4:
      break
print("You took", count , "chances")
