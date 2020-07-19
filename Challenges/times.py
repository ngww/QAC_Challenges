def timestable(y):
    x = 1
    for i in range(1, y+1):
        for i in range(1, y+1):
            print(x*i, end='\t')
        print("")
        x+=1

y = int(input("Enter a number: "))
timestable(y)