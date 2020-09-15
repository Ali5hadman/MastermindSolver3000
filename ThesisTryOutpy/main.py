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

#itertools
def createstate():
    state=[]
    for x in range(1, 7):
        for y in range(1, 7):
            for z in range(1, 7):
                for q in range(1, 7):
                    state.append([x, y, z, q])
    return state



def findmin(maxscore):
    min = 1000000
    for i in range(len(maxscore)):
        if min > maxscore[i][1]:
            min = maxscore[i][1]
    return min


    ##################################################################    ##################################################################
def nextguess():
    listofmaxes=[]
    max=0
    maxscore = []
    result4score = [[], ['W'], ['W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W', 'W'], ['B'], ['B', 'W'], ['B', 'W', 'W'],
                    ['B', 'W', 'W', 'W'], ['B', 'B'], ['B', 'B', 'W'], ['B', 'B', 'W', 'W'], ['B', 'B', 'B'],
                    ['B', 'B', 'B', 'B']]
    score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for a in range(len(allstate)):
        for b in range(len(state)):
            #print('the A values will be :' + str(a))
            #print('thr B value will be : '+ str(b))
            resultscore = checkcode(state[b], allstate[a])  # code,guess
            #print("resul code: " +str(resultscore))
            score[result4score.index(resultscore)] += 1
            #print('score = ' + str(score))

        for s in range(len(score)):
            if max < score[s]:
                max = score[s]
        maxscore.append([allstate[a], max])

        score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        max=0


    #print('the max scores are '+ str(maxscore))
    #print('the listofmax values are '+str(listofmaxes))

    min=findmin(maxscore)
    #print('the min is '+str(min))
    nextg=[]
    for i in range(len(maxscore)):
        if min == maxscore[i][1]:
            nextg.append(maxscore[i])
    nextguesss=nextg[0][0]
    #print('the final result is '+ str(nextg))

    for i in range(len(nextg)):
        if nextg[i][0] in state:
            nextguesss=nextg[i][0]
            break

    #return nextg
    return nextguesss




    ##################################################################    ##################################################################v





state=createstate()
allstate= createstate()
code= getcode()
guess = [1,1,2,2]


c=0
won=False
while won == False:
    c=c+1
    print("Turn"+str(c)+" ======================================")
    print("code =  "+str(code))
    print("guess = " + str(guess))
    result=checkcode(code,guess)
    print("result = "   + str(result))
    counter=[]
    for i in range(len(state)):
        tempresult =checkcode(state[i],guess)
        if tempresult != result:
            counter.append(state[i])

    for i in range(len(counter)):
        state.remove(counter[i])


    #print('len of counter = ' + str(len(counter)))
    #print("len of state = "+str(len(state)))
    #print("current states left = "+ str(state))
    if result == ['B','B','B','B']:
        won=True
    else:
        guess=nextguess()
