import sys

welcomemessage = "Select a difficulty for the fill-in-the-blank quiz you are about to play!"

allanswers = [["Dunkirk", "Christopher", "British", "beach", "German"],
              ["musical", "composed", "Zimmer", "ticking", "pocket"],
              ["IMAX", "quality", "Master", "Hateful"]]

blanks1 = ["__1__", "__2__", "__3__", "__4__", "__5__"]



quizes = ["The movie __1__ is a war movie directed by __2__ Nolan about the __3__ and French armies stranded on the __4__ of Dunkirk while the __5__ army closed in on them.",
          "The __1__ score for Dunkirk was __2__ by Hans __3__. In the score, there is a __4__ sound that serves as a crucial theme of the film. The noise was directly recorded using Christopher Nolan's __5__ watch.",
          "In the movie Dunkirk, Christopher Nolan shot the entire movie in 70mm __1__ film in order to achieve the maximum image __2__. Two other movies, The __3__ and The __3__ Eight were the only other two films to be shot and shown in this format in the 2010's."]


easyquiz = quizes[0]
mediumquiz = quizes[1]
hardquiz = quizes[2]


selectedLevel = 0



print welcomemessage


def blank_in_quiz(blank, blanks):
    for bl in blanks:
        if bl in blank:
            return bl
    return None

def play_game(ml_string, blanks, selectedLevel):


    replaced = []
    ml_string = ml_string.split()
    currentQuestion = 0


    for blank in ml_string:
        replacement = blank_in_quiz(blank, blanks,)
        if replacement != None:
            user_input = raw_input("\nType in the answer for blank \n" + replacement + " ")
            while user_input != allanswers[selectedLevel][currentQuestion]:
                print "Incorrect!"
                user_input = raw_input("Type in the answer for blank " + replacement + " ")
            else:
                blank = blank.replace(replacement, user_input)
                replaced.append(blank)
                print "\nCorrect!\n"
                print " ".join(replaced)
                currentQuestion = currentQuestion + 1
        else:
            replaced.append(blank)
    replaced = " ".join(replaced)
    print replaced


def difficultyselect():
    userinput = raw_input("\nPlease enter a difficulty: easy, medium, or hard. Type quit to leave:\n")
    if userinput == "easy":
        print easyquiz
        selectedLevel = 0
        play_game(easyquiz, blanks1, selectedLevel)
        difficultyselect()
    if userinput == "medium":
        print mediumquiz
        selectedLevel = 1
        play_game(mediumquiz, blanks1, selectedLevel)
        difficultyselect()
    if userinput == "hard":
        print hardquiz
        selectedLevel = 2
        play_game(hardquiz, blanks1, selectedLevel)
        difficultyselect()
    if userinput == "quit":
        sys.exit(0)
    else:
        print "That is not a valid difficulty"
        difficultyselect()


difficultyselect()
