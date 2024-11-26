# Tutorial7

import random

#q means question number
q=1

#record the marks
marks=0

#set lives
lives=3

while q<=10: # It means there will be 10 questions

    if lives == 0: # If you get wrong for 3 times, you will lose.
        break

    elif q == 10: # It means it finished
        print("YOU WIN!")
        print("Your score is", marks, "out of 10")
        break

    else:
        print("Question", q)
        s = random.randint(1, 4) # s means the symbol like plus, minus etc.

        if s == 1: # it means x+y
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            print("What is",x,"+",y,"?")
            answer=int(input(">"))
            if answer == x+y:
                print("CORRECT!")
                marks += 1
                q += 1
            else:
                print("WRONG!")
                lives -= 1
                q += 1

        elif s == 2: # it means x-y
            x = random.randint(1,12)
            y = random.randint(1,12)
            print("What is",x,"-",y,"?")
            answer=int(input(">"))
            if answer == x - y:
                print("CORRECT!")
                marks += 1
                q += 1
            else:
                print("WRONG!")
                lives -= 1
                q += 1

        elif s == 3: # it means x*y
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            print("What is",x,"*",y,"?")
            answer = int(input(">"))
            if answer == x*y:
                print("CORRECT!")
                marks += 1
                q += 1
            else:
                print("WRONG!")
                lives -= 1
                q +=1

        elif s == 4: # it means x/y
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            print("What is",x*y,"/",y) # the answer must be integer
            answer = int(input(">"))
            if answer == x:
                print("CORRECT!")
                marks += 1
                q += 1
            else:
                print("WRONG!")
                lives -= 1
                q += 1

quit()
