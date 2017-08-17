welcomemessage = "Select a difficulty for the fill-in-the-blank quiz you are about to play!"

easydiff = "The movie __1__ is a war movie directed by __2__ Nolan about the __3__ and French armies stranded on the __4__ of Dunkirk while the __5__ army closed in on them."
easyanswers = ["Dunkirk", "Christopher", "British", "beach", "German"]

mediumdiff = "The __1__ score for Dunkirk was __2__ by Hans __3__. In the score, there is a __4__ sound that serves as a crucial theme of the film. The noise was directly recorded using Christopher Nolan's __5__ watch."
mediumanswers = ["musical", "composed", "Zimmer", "ticking", "pocket"]

harddiff = "In the movie Dunkirk, Christopher Nolan shot the entire movie in 70mm __1__ film in order to achieve the maximum image __2__. Two other movies, The __3__ and The __3__ Eight were the only other two films to be shot and shown in this format in the 2010's."
hardanswers = ["IMAX", "quality", "Master", "Hateful"]

allanswers = ["Dunkirk", "Christopher", "British", "beach", "German", "musical", "composed", "Zimmer", "ticking", "pocket", "IMAX", "quality", "Master", "Hateful"]

blanks = ["__1__", "__2__", "__3__", "__4__", "__5__"]

print welcomemessage

#def selectdiff():
#    userinput = raw_input("Type easy, medium, or hard")
#    if userinput == "easy":
#        easy()
#    elif userinput == "medium":
#        medium()
#    elif userinput == "hard":
#        hard()
#    else:
#        print "That is not a valid difficulty."


#def easy(easyquiz):
#    print easyquiz
#    print
#    print "Fill in the blanks with the correct answer."
#    print "Capitlization counts!"

def blank_in_quiz(blank, blanks):
    for blank in blanks:
        if blank in quiz:
            return blank
    return None

def play_game(ml_string, blanks):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = blank_in_quiz(blank, blanks)
        if replacement != None:
            user_input = raw_input("Type in a answer for blank: " + replacement + " ")
            blank = blank.replace(replacement, user_input)
            replaced.append(word)
        elif replacement == allanswers:
            print "Correct!"
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(easydiff, blanks)
