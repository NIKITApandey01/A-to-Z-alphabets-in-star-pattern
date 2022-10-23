for row in range(5):
    for col in range(3):
        if((row>=0 or row<=4)  and col==0) or ((row==0 or row==2 ) and (col==2 or col==1)):
            print("*",end="")
        else:
            print(end=" ")
    print()
        