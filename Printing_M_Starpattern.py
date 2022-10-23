for row in range(5):
    for col in range(11):
        if((row==0 and(col==0 or col==1 or col==9 or col==10)) or
         (row==1 and (col==0 or col==2 or col==8 or col==10)) or
         (row==2 and (col==0 or col==3 or col==7 or col==10)) or
         (row==3 and (col==0 or col==4 or col==6 or col==10) or
         (row==4 and(col==0 or col ==4 or col==5 or col==10)))):
           print("*",end="")
        else:
            print(end=" ")
    print()

            


        

