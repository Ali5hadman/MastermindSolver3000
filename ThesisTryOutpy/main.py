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



state=createstate()
allstate= createstate()
code= getcode()
guess = [1,1,2,2]
c=0
won=False
while won==False:
    c=c+1
    print("Turn"+str(c)+" ======================================")
    print("code =  "+str(code))
    print("guess = " + str(guess))
    result=checkcode(code,guess)
    print("result = "   + str(result))
    y= len(state)

    for i in state:
      tempresult =tempcheckcode(i,guess)
      if tempresult != result:
          state.remove(i)
      tempresult.clear()
    x= len(state)
    print('Number of codes eliminated = '+ str(y-x))
    print("len of state = "+str(len(state)))
    print("current state = "+ str(state))
    if result == ['B','B','B','B']:
        won=True
    else:
        numberofscore=0
        for a in range(len(allstate)):
            for b in range(len(state)):
                resultscore=tempcheckcode(allstate[a], state[b])
                if resultscore != []:
                    numberofscore=numberofscore+1
                    

        guess = state[0]
    result.clear()
























