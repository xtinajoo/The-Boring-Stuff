import random #1
def getAnswer (answerNumber): #2
    if answerNumber == 1: #3
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber ==3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Very doubtful'
r=random.randint(1,9)#4
fortune = getAnswer(r)#5
print (fortune)#6

#Lines 4,5,6 can be shortened to: print (getAnswer(random.randint(1,9))
