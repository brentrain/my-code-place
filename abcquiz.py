from question import question

question_prompts = [
    "What color is the sky? \n(a) blue \n(b) red \n (c) yellow\n\n",
    "How many months are in a year? \n(a) 14 \n (b) 12 \n (c) 76\n\n"
    "Why did the chicken cross the road?\n (a) to get to the other side \n (b)\
     fear \n (c) food\n\n"]

questions = [
    question(question.prompts[0], "a"),
    question(question.prompts[1], "b"),
    question(question.prompts[2], "a"),
]


def run_test(question):
    score = 0
    for questions in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1


print("You got " + (score) + "/" + str(len(questions)) + "correct!")


run_test(questions)
