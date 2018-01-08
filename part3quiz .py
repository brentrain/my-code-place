
# The program is required to have 4 blanks
blankS = [" ___1___ ", " ___2___ ", " ___3___ ", " ___4___ ", "___5___"]

# easy fill in the blanks
easy_questions = ["Question 1","Question 2", "Question 3", "Question 4", "Question 5"]
easy_answers = ["Answer 1", "Answer 2", "Answer 3", "Answer 4", "Answer 5"]

# medium fill in the blanks
medium_questions = "Question 1. Question 2. Question 3. Question 4."
medium_answers = ["answer 1", "answer 2", "answer 3", "answer 4", "answer 5"]

# difficult fill in the blank
hard_questions = "Question 1. Question 2. Question 3. Question 4."
hard_answers = ["answer 1", "answer 2", "answer 3", "answer 4", "answer 5"]

##----------##
##----------##

# Quiz level selection


def choose_level():
    level = raw_input("Please select one of the following levels: Easy, Medium, or Hard: ").lower()
    if level == "easy":
        return quiz(easy_questions, easy_answers)
    if level == "medium":
        return quiz(medium_questions, medium_answers)
    if level == "hard":
        return quiz(hard_questions, hard_answers)
    else:
        return choose_level()

##----------##
##----------##

# Checks to see if numbered_blanks is a substring of both blank list and questions.


def search_for(blank_numbers, questions):
    for new_answer in questions:
        if new_answer in blank_numbers:
            return new_answer
    return None

##----------##
##----------##

# Replace blanks with correct answers


def process_question(questions):
    replaced = []
    questions = questions.split()
    for blanks in questions:
        # print blanks
        replacement = search_for(blank_numbers, questions)


    if replacement != None:
            blanks = blanks.replace(replacement, fill_blank)
            replaced.append(blanks)
    else:
            replaced.append(blanks)
            replaced = " ".join(replaced)
            return replaced


##----------##
##----------##


# Prompt for answers, if correct moves to next question if wrong counts

def quiz(questions, answers):
    index = 0
    print (questions)
    try_again = 0

    while index < len(answers):
        for new_answer in blank_numbers:
            fill_blank = raw_input("Please fill in blank " + new_answer + ": ").lower()
            if fill_blank == answers[index]: # Checking to see if users answer matches
                index = index + 1 # If answers match move to next fill in blank
                processing = process_question(questions) #replacing users input in the paragraph
            else:
                try_again = try_again + 1
                if try_again < 4:
                    print "Try again"
                else:
                    print "Quiz over"
                    break
pick_level()
