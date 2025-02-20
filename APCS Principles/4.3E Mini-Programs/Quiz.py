# VvSeanGtvV 2025-2026
import random as rand
questionList = ["Is Python easy?|true",
"Is Python similar to Java?|true",
"Is Scratch hard?|false",
"Does the array in Python starts at 0?|true",
"Is Array in Scratch similar to Python?|true"]

falseMulti = ["f", "false"]
trueMulti = ["t", "true"]
def getKey(get):
    key = 0
    data = questionList[get]
    q = a = ""
    for st in data:
        if (st == "|"):
            key = 1
        if (key == 0):
            q = q + st
        else:
            if (st != "|"):
                a = a + st
    return q, a

def getAns(usr, ans):
    if (ans == "false"):
        if (usr.lower()) in falseMulti:
            return 1
        elif (usr.lower()) in trueMulti:
            return 0
        else:
            return 2
    else:
        if (usr.lower()) in trueMulti:
            return 1
        elif (usr.lower()) in falseMulti:
            return 0
        else:
            return 2

def game(q):
    if (q >= len(questionList)):
        game(rand.randint(0, 1))
    else:
        question, answer = getKey(q)
        user = input(question + " True or False: ")
        ky = getAns(user, answer)
        if (ky != 2):
            if (ky == 1):
                print("CORRECT")
                game(q + rand.randint(1, 2))
            else:
                print("WRONG")
                game(q + rand.randint(1, 2))
        else:
            print("INVALID ANSWER")
            game(q)
        
game(rand.randint(0, 1))
