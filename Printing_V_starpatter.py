for row in range(4):
    for col in range(3):
        if(((row>=0 and row<=2) and (col==0 or col==2)) or ( row==3 and col==1)):
            print("*",end="")
        else:
            print(end=" ")
    print()