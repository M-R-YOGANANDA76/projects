import random as r
def table(sum1):#for table
    n=1
    m=10
    for i in range(1,10+1):
        for j in range(n,m+1):
            if j==m:
                if sum1==j:
                    print("$$$")
                else:
                    print(j)
            else:
                if sum1==j:
                    print("$$$",end="  ")
                else:
                    print(j,end="  ")
        n=j+1
        m=m+10
def table(sum2):
    n=1
    m=10
    for i in range(1,10+1):
        for j in range(n,m+1):
            if j==m:
                if sum2==j:
                    print("###")
                else:
                    print(j)
            else:
                if sum2==j:
                    print("###",end="  ")
                else:
                    print(j,end="  ")
        n=j+1
        m=m+10        

sum1=0
sum2=0
num=1
b=0
while 1==1: #game runner
    score=r.randint(1,6)
    a=int(input("enter player number"))
    if b==a:
        print("single player cannot be played twice")
        continue
    if a==1 or a==2:
        b=a
        if a==1:
            print("player1 score=",score)
            if (sum1+score)<=100:
                sum1=sum1+score
                print(sum1)
                table(sum1)
            else:
                continue
        else:
            print("player2 score=",score)
            if (sum2+score)<=100:
                sum2=sum2+score
                print(sum2)
                tabl(sum2)
            else:
                continue
#snake to reduce the number
    if sum1==51:
        sum1==sum1-20
    elif sum1==15:
        sum1==sum1-5
    elif sum1==13:
        sum1==sum1-10
    elif sum1==75:
        sum1==sum1-40
    elif sum1==98:
        sum1==sum1-35
    if sum2==51:
        sum2==sum2-20
    elif sum2==15:
        sum2==sum2-5
    elif sum2==13:
        sum2==sum2-10
    elif sum2==75:
        sum2==sum2-40
    elif sum2==98:
        sum2==sum2-35
#ladder to boost the number
    if sum1==21:
        sum1==sum1+20
    elif sum1==27:
        sum1==sum1+15
    elif sum1==19:
        sum1==sum1+25
    elif sum1==60:
        sum1==sum1+33
    elif sum1==28:
        sum1==sum1+27
    if sum2==21:
        sum2==sum2+20
    elif sum2==27:
        sum2==sum2+15
    elif sum2==19:
        sum2==sum2+25
    elif sum2==60:
        sum2==sum2+33
    elif sum2==28:
        sum2==sum2-27
#note
    print("*NOTE  \n SNAKES \n 51-31\n15-10\n13-3\n75-35\n98-63")
    print("*NOTE  \n ladders\n 21-41\n27-42\n19-44\n60-93\n28-55")
#to check the winner
    if sum1>=100:
        print("player 1 is winner")
        break
    if sum2>=100:
        print("player 2 is winner")
        break
