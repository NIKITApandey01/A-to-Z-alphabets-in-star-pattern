for row in range(5):
    for col in range(3):
        if (((row>=0 or row<=4) and col==0) or ((row==0 or row==2) and col==1) or ((row>=0 and row<=2) and col==2)):
            print("*",end="")
        else:
            print(end=" ")
    print()