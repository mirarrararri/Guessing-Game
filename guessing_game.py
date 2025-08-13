name = input("Enter Your Name: ")
print(f"Welcome to Guessing Game!, {name}")

corrAns = "206"
lives = 3

while lives > 0:
    ans = input("\nGuess how many bones have an adult human body?: ")
    lives -= 1
    if  corrAns == ans:
        print("Message: CONGRATUALATION YOUR ANSWER IS CORRECT!")
        break
    else:
        print("Message: INCORRECT, Please try again")
        if lives >= 2:
            print(f"Lives: {lives} left")
        else:
            print(f"Live: {lives} left")
else:
    print("\nMessage: Sorry you only have 3 lives")