#A message to greet the user
welcomemessage = "Select a difficulty for the fill-in-the-blank quiz you are about to play! NOTE: Capitilizations matter!"

# A list of all of the answers for the easy, medium, and hard quiz in a list of lists
allanswers = [["Dunkirk", "Christopher", "British", "beach", "German"],
              ["musical", "composed", "Zimmer", "ticking", "pocket"],
              ["IMAX", "quality", "Master", "Hateful", "2010"]]

# A list of all of the quizes in order from easy to hard
quizes = ["The movie __1__ is a war movie directed by __2__ Nolan about the __3__ and French armies stranded on the __4__ of Dunkirk while the __5__ army closed in on them.",
          "The __1__ score for Dunkirk was __2__ by Hans __3__. In the score, there is a __4__ sound that serves as a crucial theme of the film. The noise was directly recorded using Christopher Nolan's __5__ watch.",
          "In the movie Dunkirk, Christopher Nolan shot the entire movie in 70mm __1__ film in order to achieve the maximum image __2__. Two other movies, The __3__ and The __4__ Eight were the only other two films to be shot and shown in this format in __5__."]


# The user is prompted to enter a difficulty, once done, the function returns an integer to use. This integer then associates the quiz
def difficulty():
    userinput = raw_input("\nPlease enter a difficulty: easy, medium, or hard. Type quit to leave:\n")
    if userinput == "easy":
        return 0
    if userinput == "medium":
        return 1
    if userinput == "hard":
        return 2
    else:
        print "That is not a valid difficulty"
        difficulty()

# finds the blank in the quiz, then replaces the user's correct answer in it. The function then returns the entire
# quiz with the user's answer, as well as the rest of the quiz and the blanks.
def restofquiz(answer, quiz, index):
    blank = "__" + str(index + 1) + "__"
    restofquestion = quiz.replace(blank, answer)
    return restofquestion

# grades the user's input and checks it if it equals the list of allanswers
def grade(user_input, answer):
    if user_input == answer:
        return True
    else:
        return False

# starts the quiz
def start(quiz):
    index = 0
    # number of blanks in each quiz
    blanks = 5
    # a loop that checks if the index is less than the number of blanks
    while index < blanks:
        # prints the quiz
        print(quiz+"\n")
        answer = (allanswers[difficulty][index])
        # asks the user to type in the answer
        user_input = raw_input("Type in the answer for blank "+ str(index + 1)+ " ")
        # goes to the function grade, if the answer is correct, it replaces the answer in the blank
        if grade(user_input, answer):
            quiz = restofquiz(answer, quiz, index)
            index += 1
            print "Correct!"
        else:
            print "Incorrect, try again!"

print welcomemessage
difficulty = difficulty()
quiz = quizes[difficulty]
start(quiz)
