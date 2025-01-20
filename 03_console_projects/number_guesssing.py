import random as r
random_number = r.randrange(1, 15) # generating a random number according to our defined range

def start_game():
    score = 1000
    guess = int(input("Guess: "))
    tries = 1
    while guess != random_number:
        if 0 < guess < 15:
            if guess > random_number:
                print("Lower")
            else: 
                print("Higher")
            score = score - 100
            guess = int(input("Guess: "))
        else: 
            print("Out of range (1 - 14) guess.")
            score -= 50
            guess = int(input("Guess: "))
        tries+=1

    if 1 <= tries < 4:
        score += 100
    elif 4 <= tries < 7:
        score += 50
            
    print(f"You guessed the number in {tries} tries. Your score is {score}!")


def main():
    print("Welcome to Password Game\n\n\tThe computer has randomly chosen a number between 1 - 14.\n")
    play = input("Do you want to guess the number? (y/n): ")

    start_game() if play == 'y' else exit(0)

main()