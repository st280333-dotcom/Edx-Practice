import random

def run_guessing_game():
    secret_number = random.randint(1, 50)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 50.")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try higher.\n")
            elif guess > secret_number:
                print("Too high! Try lower.\n")
            else:
                print(f"Correct! You found it in {attempts} attempt(s).")
                break
        except ValueError:
            print("Please enter a valid whole number.\n")


# --- Run the Task ---
run_guessing_game()