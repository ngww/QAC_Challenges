#Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)
#Write a test for this function

def addition(input):
    n1 = input
    n2 = str(input) + str(input)
    n3 = str(input) + str(input) + str(input)
    n4 = str(input) + str(input) + str(input) + str(input)
    n5 = int(n1) + int(n2) + int(n3) + int(n4)
    
    return n5