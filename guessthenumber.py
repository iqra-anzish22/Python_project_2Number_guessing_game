import random

def guess_the_number():
    """Guess the number game by computer."""
    number = random.randint(1, 100)  
    guesses_left = 7  

    print("\n Welcome to the Number Guessing Game!")
    print("\n 🔢 A number between 1 and 100 is on my mind. What's your guess?")
    
    while guesses_left > 0:
        print(f"\nOnly {guesses_left} tries left! Make it count!")

        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("❌ Invalid input! Please Enter a Valid Number.")
            continue  

       
        if guess < number:
            print("📉 Too low! Try a higher number.")
        elif guess > number:
            print("📈 Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed the correct number {number} in {7 - guesses_left + 1} tries! 🎉")
            return 
        guesses_left -= 1  

    print(f"\n❌ You ran out of guesses! The correct number was {number}. Better luck next time!")


    print("\n🔒 Logging out... Thanks for playing!\n")


guess_the_number()
