import random


def getcode():
    code=[]
    for i in range(4):
        code.append(random.randint(1,6))
    return code

def checkcode(code,guess):
    result =[]
    for i in range (4):
            if guess[i] == code[i]:
                result.append('B')
                code[i] *= -1
                guess[i] *= -1
    for i in range(4):
        if guess[i]>0:
             for j in range(4):
                    if guess[i]==code[j]:
                        result.append('W')
                        code[j]*=-1
                        break

    for i in range(4):
        if guess[i]<0:
            guess[i]*=-1
        if code[i]<0:
            code[i]*=-1
    return result


def createstate():
    state=[]
    for x in range(1, 7):
        for y in range(1, 7):
            for z in range(1, 7):
                for q in range(1, 7):
                    state.append([x, y, z, q])
    x=len(state)
    print(x)
    return state

def tempcheckcode(code,guess):
    tempresult=[]
    for i in range (4):
            if guess[i] == code[i]:
                tempresult.append('B')
                code[i] *= -1
                guess[i] *= -1
    for i in range(4):
        if guess[i]>0:
             for j in range(4):
                    if guess[i]==code[j]:
                        tempresult.append('W')
                        code[j]*=-1
                        break

    for i in range(4):
        if guess[i]<0:
            guess[i]*=-1
        if code[i]<0:
            code[i]*=-1
    return tempresult


def findmin(maxscore):
    min = 1000000
    for i in range(len(maxscore)):
        if min > maxscore[i][1]:
            min = maxscore[i][1]
    return min



def nextguess():
    min = 1000000
    max=0
    maxscore = []
    result4score = [[], ['W'], ['W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['B'], ['B', 'W'], ['B', 'W', 'W'],
                    ['B', 'W', 'W', 'W'], ['B', 'B'], ['B', 'B', 'W'], ['B', 'B', 'W', 'W'], ['B', 'B', 'B'],
                    ['B', 'B', 'B', 'B']]
    score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for a in state:
        for b in allstate:
            resultscore = tempcheckcode(a, b)  # code,guess
            score[result4score.index(resultscore)] += 1

        for s in range(len(score)):
            if max < score[s]:
                max = score[s]
        maxscore.append([a, max])

        score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        max=0
    print('the max scores are '+ str(maxscore))
    min=findmin(maxscore)
    print('the min is '+str(min))
    for i in range(len(maxscore)):
        if min == maxscore[i][1]:
            nextg = maxscore[i]
            break
    nextguesss=nextg[0]
    print('the final result is '+ str(nextg))
    print('the next guess is '+ str(nextguesss))
    return nextguesss









state=createstate()
allstate= createstate()
code= getcode()
guess = [1,1,2,2]
c=0
won=False
while won == False:
    state.remove(guess)
    allstate.remove(guess)
    c=c+1
    print("Turn"+str(c)+" ======================================")
    print("code =  "+str(code))
    print("guess = " + str(guess))
    result=checkcode(code,guess)
    print("result = "   + str(result))

    for i in state:
      tempresult =tempcheckcode(i,guess)
      if tempresult != result:
          state.remove(i)
    print("len of state = "+str(len(state)))
    print("current state = "+ str(state))
    if result == ['B','B','B','B']:
        won=True
    else:
        guess= nextguess()



