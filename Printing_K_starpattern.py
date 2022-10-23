for row in range(5):
    for col in range(4):
        if(((row>=0 or row<=4) and col==0) or ((row==1 or row==3) and col==1) or ((row==0 or row==4 )and col==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()