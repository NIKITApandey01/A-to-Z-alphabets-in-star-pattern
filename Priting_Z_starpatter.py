for row in range(5):
    for col in range(3):
        if ((row==0 or row==4 or row==2 ) and (col>=0 and col<=2) or (row==1 and col==2) or (row==3 and col==0)):
            print("*",end="")
        else:
            print(end=" ")
    print()