welcomemessage = "Select a difficulty for the fill-in-the-blank quiz you are about to play!"

allanswers = ["Dunkirk", "Christopher", "British", "beach",
              "German", "musical", "composed", "Zimmer",
              "ticking", "pocket", "IMAX", "quality", "Master", "Hateful"]

blanks = ["__1__", "__2__", "__3__", "__4__", "__5__"]


quizes = ["The movie __1__ is a war movie directed by __2__ Nolan about the __3__ and French armies stranded on the __4__ of Dunkirk while the __5__ army closed in on them.",
          "The __1__ score for Dunkirk was __2__ by Hans __3__. In the score, there is a __4__ sound that serves as a crucial theme of the film. The noise was directly recorded using Christopher Nolan's __5__ watch.",
          "In the movie Dunkirk, Christopher Nolan shot the entire movie in 70mm __1__ film in order to achieve the maximum image __2__. Two other movies, The __3__ and The __3__ Eight were the only other two films to be shot and shown in this format in the 2010's."]


easyquiz = quizes[0]
mediumquiz = quizes[1]
hardquiz = quizes[2]

def playquiz():
    userinput = raw_input("Please enter a difficulty: easy, medium, or hard")
    if userinput == "easy":
        easy()
    elif user_input == "medium":
        medium()
    elif user_input == "hard":
        hard()
    else:
        print "That is not a valid input"
        playquiz()

def easy():
    print easyquiz

playquiz()
