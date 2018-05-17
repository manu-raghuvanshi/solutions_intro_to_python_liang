#Rock, Paper, Scissor Game
import random
u = 0 #user win count
c = 0 #computer win count
while u<3 and c<3: #As soon as someone wins 
    user = eval(input("Choose 1 for rock, 2 for paper and 3 for scissor"))
    comp = random.randint(1,3)
    if user==1 and comp==1:
        print("User chooses Rock and Computer chooses Rock. It's a tie, Go again!!")
    elif user==1 and comp==2:
        print("User chooses Rock and Computer chooses Paper. Computer Wins!!")
        c += 1
    elif user==1 and comp==3:
        print("User chooses Rock and Computer chooses Scissor. User Wins!!")
        u += 1
        
        
    elif user==2 and comp==2:
        print("User chooses Paper and Computer chooses Paper. It's a tie, Go again!!")
    elif user==2 and comp==1:
        print("User chooses Paper and Computer chooses Rock. User Wins!!")
        u += 1
    elif user==2 and comp==3:
        print("User chooses Paper and Computer chooses Scissor. Computer Wins!!")
        c += 1
        
        
    elif user==3 and comp==3:
        print("User chooses Scissor and Computer chooses Scissor. It's a tie, Go again!!")
    elif user==3 and comp==2:
        print("User chooses Scissor and Computer chooses Paper. User Wins!!")
        u += 1
    elif user==3 and comp==1:
        print("User chooses Scissor and Computer chooses Rock. Computer Wins!!")
        c += 1
        
        
if u>2:
    print("User Wins!!!")
else:
    print("Computer Wins!!!")