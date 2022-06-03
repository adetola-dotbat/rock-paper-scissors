import random

user_score = int(0)
pc_score = int(0)
score_limit = 5

def user_input(user_guess):
    
    user_guess = user_guess.lower()
    return user_guess

while user_score != score_limit or pc_score != score_limit:
    user_guess: str = input(str("pls enter your guess, \"r\" for rock \"p\" for paper \"s\" for scissors:"))
    user_input(user_guess)
    
    user_guessing = user_input(user_guess)
    print("Player input is:", user_guessing)
    my_list = ["r", "p", "s"]
    pc_guess = random.choice(my_list)
    print("The computer chose", pc_guess)

    if pc_guess == "r" and user_guessing == "r":
        print ( "COM: {} and Player: {}" .format(pc_guess, user_guessing),  "So, it is a Tie!!" )

    if pc_guess == "p" and user_guessing == "p":
        print ( "COM: {} and Player: {}" .format(pc_guess, user_guessing),  "So, it is a Tie!!" )

    if pc_guess == "s" and user_guessing == "s":
        print ( "COM: {} and Player: {}" .format(pc_guess, user_guessing),  "So, it is a Tie!!" )

    if pc_guess == "p" and user_guessing == "r":
        pc_score = int ( pc_score ) + 1
        print ( "COM: {} and Player: {}." .format(pc_guess, user_guessing), "The pc score is:", pc_score )

    if pc_guess == "r" and user_guessing == "p":
        user_score = int (user_score) + 1
        print ( "COM: {} and Player: {}." .format(pc_guess, user_guessing), "Your score is:", user_score )

    if pc_guess == "r" and user_guessing == "s":
        pc_score = int ( pc_score ) + 1
        print ( "COM: {} and Player: {}." .format(pc_guess, user_guessing), "The pc score is:", pc_score )

    if pc_guess == "s" and user_guessing == "r":
        user_score = int (user_score) + 1
        print ( "COM: {} and Player: {}." .format(pc_guess, user_guessing), "Your score is:", user_score )

    if pc_guess == "p" and user_guessing == "s":
        user_score = int (user_score) + 1
        print ( "COM: {} and Player: {}." .format(pc_guess, user_guessing), "Your score is:", user_score )

    if pc_guess == "s" and user_guessing == "p":
        pc_score = int ( pc_score ) + 1
        print ( "COM: {} and Player: {}." .format(pc_guess, user_guessing), "The pc score is:", pc_score )
        pc_guess = random.choice ( my_list )

    if user_score == score_limit:
        print("Hurray! you won")

        break

    elif pc_score == score_limit:
        print("oopsies, the computer won, better luck next time")

        break
