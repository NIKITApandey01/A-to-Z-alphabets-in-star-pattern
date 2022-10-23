for row in range(5):
    for col in range(5):
        if (((row==0 or row==4) and (col==0 or col==4)) or ((row==1 or row==3) and (col==1 or col==3)) or (row==2 and col==2) ):
            print("*",end="")
        else:
            print(end=" ")
    print()