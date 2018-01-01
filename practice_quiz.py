# define variables

quiz1 = "brent"
quiz2 = "brent4"
quiz3 = "Rainwater"
error = "Sorry, Try again"

number_of_attempts = 3


def choose_quiz():
    # prompts the player to choose a level of difficulty
    while number_of_attempts == 0:
        # sets the number of attempts to zero
        user_input = raw_input()
            print "Welcome to my quiz!"
            time.sleep(1)
            print "Please select a difficulty level: 1 for Easy, 2 for Medium or 3 for Difficult:"
    if user_input == "1":
        return quiz1
        x = 0
    else:
        if user_input == "2":
            return quiz2
            x = 0
    else:
        if user_input = "3":
            return quiz3
            x = 0

    else:
        return error
