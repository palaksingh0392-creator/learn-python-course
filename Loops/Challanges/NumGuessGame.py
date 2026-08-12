# Challenge 2: Number Guessing Game
#  Use a secret number between 1 and 100.
#  The user keeps guessing.
#  Display Too High, Too Low or Correct.
#  Count how many attempts the user used.

num = 45
count = 0
while True:
    guess = int(input("enter your guessing no."))
    count +=1
    if guess > num :
        print("too high")
    elif guess < num :
        print("too low")
    elif guess == num :
        print("correct")
        break
print(f"you guessed the no. in {count} - counts")

