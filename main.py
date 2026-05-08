import random

number = random.randint(1, 100)

print("===== Number Guessing Game =====")
print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Yehe Correct! You have won!")
        break

    difference = abs(number - guess)

    if difference <= 5:
        print("🔥 Very close!")
    elif difference <= 10:
        print("⚡ Close! Try again.")
    else:
        print("❌ Far away!")

    if guess < number:
        print("⬆ Go Higher!\n")
    else:
        print("⬇ Go Lower!\n")