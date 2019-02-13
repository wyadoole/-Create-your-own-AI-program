# The library that this program using is Textblob so it can do sentiment for each statement
from textblob import TextBlob
# Program discription
print("This application test polarity of article that user selected based on positive = 1 or negitive = -1")
print("Also displays if the statement is nutrual with output phrase")
print("The user will chooce between 0 and 5 of the statements to test")

# The program uses the default list so the user can use as input -> 6 sentences to use inout 0,1,2,3,4,5
defualtList = ["(0) Pizza is the best type of food", "(1) I hate pizza", "(2)I like cake", "(3) Reading magazines is fun", "(4) I hate every video game", "(5) I like the Metrix movies"]
print(defualtList) # uses the precreated list to print to screen 

# The user chooces what sentance to use to test the polarity of
userChoice = int(input("choose any sentence from the list"))
chosenSentence = defualtList[userChoice]

# analysis if the statement is positive or negetive else nutrual
print(chosenSentence) # prints the users chosen sentence
analysis = TextBlob(chosenSentence) # sets what the alalysis is for the program

if analysis.sentiment[0] > 0: # checks to see what the plarity is for the chosen text 
    oppisiteText = "" # calls the opposite string of the chosen text
    for i in defualtList: # goe thorugh the list of sentances 
        text = TextBlob(i) # calls the ploarity using textblob library 
        if text.sentiment[0] < 0:# is polarity is < defualt sentence then the Ai is supose to get the negative or return output phrase 
            oppisiteText = i # calls for opposite sentence that has not been chosen 
    print("here is a recommendation for you: ", oppisiteText)
    """prints the oppiste of the users selection based on polarity of 1 or -1 of statement"""

elif analysis.sentiment[0] < 0: # checks to see what the plarity is for the chosen text
    oppisiteText = "" # calls the opposite string of the chosen text that has not been used 
    for i in defualtList: # goe thorugh the list of sentances 
        text = TextBlob(i) # calls the ploarity using textblob library 
        if text.sentiment[0] > 0: # is polarity is > defualt sentence then the Ai is supose to get the negative or return output phrase 
            oppisiteText = i # calls for opposite sentence that has not been chosen 
    print("here is a recommendation for you: ", oppisiteText)
    """prints the oppiste of the users selection based on polarity of 1 or -1 of statement"""
else:
    print("found a good article")
    print("neutral -> no polarity detected")
# prints out nutrual result based on the polarity of the sentence that the Ai found
