#--------------------
def newgame():
    qno=1
    score=0
    guesses=[]
    for key in questions:
        print(key)
        for i in options[qno-1]:
            print(i)
        
        guess=input('enter your guess A,B,C or D : ').upper()
        guesses.append(guess)
        score=score+checkans(questions.get(key),guess)
        qno=qno+1

        print('-------------------------')
    print('your score is: ', score)
    playagain()
#--------------------

def checkans(ans,guess):
    print(ans,guess,sep='\n')
    if guess==ans:
        print('correct ans')
        return 1

    else:

        print('wrong ans')
        return 0

    pass

#--------------------

def playagain():
    ch=input('do you wish to play again? y/n:').lower()
    if ch=='y' or ch=='yes':
        newgame()
    else:
        print('thank you for playing')

        
    
#--------------------

questions={'1.who am i?':'A', '2.who is my father?':'B','3.who is my mother?':'C', '4.who is my brother': 'D'}
options=[ ['A:mathew','B.kk','C.ss','D.kk'], \
          ['A:mathew','B.kk','C.ss','D.kk'], \
          ['A:mathew','B.kk','C.ss','D.kk'], \
          ['A:mathew','B.kk','C.ss','D.kk']]

newgame()