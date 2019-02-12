# The library that this program using is Textblob and the sentiment and analysis portion of that library
from textblob import TextBlob
#
print("This application test polarity of each statement with positive = 1 or negitive = -1")
print("The user will chooce between 0 and 5")
defualtList = ["Pizza is the best", "I hate pizza", "I like cake", "I reading is fun", "I hate video games", "I like the Metrix movie"]
print(defualtList)
userChoice = int(input("choose any sentence from the list"))
chosenSentence = defualtList[userChoice]
print(chosenSentence)
analysis = TextBlob(chosenSentence)
if analysis.sentiment[0] > 0:
    oppisiteText = ""
    for i in defualtList:
        text = TextBlob(i)
        if text.sentiment[0] < 0:
            oppisiteText = i
    print("here is a recommendation for you: ", oppisiteText)
elif analysis.sentiment[0] < 0:
    oppisiteText = ""
    for i in defualtList:
        text = TextBlob(i)
        if text.sentiment[0] > 0:
            oppisiteText = i
    print("here is a recommendation for you: ", oppisiteText)
else:
    print("found a good article")