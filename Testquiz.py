quiz_google = (
    "__1__ is a multinational company begun in __2__, California in __3__ by __4__ and __5__.")
answers_google = ["Google", "Mountain View", "1998", "Sergey Brin", "Larry Page"]

"""quiz about weather"""

quiz_weather = ("A __1__ is __2__ phenomenon that is caused by __3__, refraction and dispersion of __4__in water droplets resulting in a __5__.")
answers_weather = ["Rainbow", "weather", "reflection", "light", "spectrum"]

quiz_snakes = ("__1__ eat their prey whole and are able to consume prey __2__  times larger than the diameter of their __3__ because their lower __4__ can separate from the __5__ jaw.")
answers_snakes = ["Snakes", "three", "head", "jaw", "upper"]
blank_spaces = ["__1__", "__2__", "__3__", "__4__", "__5__"]


def select_quiz():

    while True:
        quiz_play = raw_input("Please, choose the quiz you want to take: "
                              "(Google, Weather or Snakes)"
        if player_quiz == "Google"
            return quiz_google
        elif:
            player_quiz == "Weather":
                return quiz_weather
        elif:
            player_quiz == "Snakes":
                return quiz_snakes
    else:
        print "Please choose one of the  current games!"

def quiz_answers():
    quiz_choice = choose_quiz()
    if player_quiz_pick == quiz_google:
        return answers_google
    elif player_quiz_pick == quiz_weather:
        return answers_weather
    elif player_quiz_pick == quiz_snakes:
        return answers_snakes
