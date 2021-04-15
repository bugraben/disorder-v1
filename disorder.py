from random import shuffle
from os import system
system("color 5f")
system("mode 100,30")
system("title disorder v1")

def getInput():
    return input(">").split()

def disorder(word):
    if len(word) <= 3:
        return word
    elif len(word) <= 7:
        wordAsList = list(word)
        newlist = wordAsList[1:-1].copy()
        while newlist == wordAsList[1:-1]:
            shuffle(newlist)
        wordAsList[1:-1] = newlist
        return ''.join(wordAsList)
    elif len(word) <= 10:
        wordAsList = list(word)
        newlist = wordAsList[3:-3].copy()
        while newlist == wordAsList[3:-3]:
            shuffle(newlist)
        wordAsList[3:-3] = newlist
        return ''.join(wordAsList)
    else:
        wordAsList = list(word)
        newlist1 = wordAsList[1:3].copy()
        newlist2 = wordAsList[3:-3].copy()
        newlist3 = wordAsList[-3:-1].copy()
        newlist = [newlist1, newlist2, newlist3]
        for i in newlist:
            shuffle(i)
        wordAsList[2:4] = newlist1
        wordAsList[4:-3] = newlist2
        wordAsList[-3:-1] = newlist3
        return ''.join(wordAsList)

while True:
    x = ' '.join(list(map(disorder, getInput())))
    print(x)
