def timestable(n):
    line = ""
    for row in range(1, y+1):
        for column in range(1, y+1):
            line += str(row * column) + "\t"
        line += "\n"
    return line

y = int(input("Enter a number: "))
print(timestable(y))