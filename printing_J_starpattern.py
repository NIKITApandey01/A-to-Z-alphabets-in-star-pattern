for row in range(4):
    for col in range(5):
        if((row==0 and (col>=0 or col<=4)) or (row==1 and col==2) or ((row==2 or row==3)and (col==0 or col==2))):
            print("*",end="")
        else:
            print(end=" ")
    print(  )