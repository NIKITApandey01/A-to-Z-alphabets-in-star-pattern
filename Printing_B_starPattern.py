for row in range(5):
    for col in range(3):
       if((col==0 or col==2) or ((col==1) and (row!=1 and row!=3))):

        print("*",end="")
        
       else:
        print(end=" ")
    print()


    
    