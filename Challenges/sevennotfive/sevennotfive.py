def sevennotfive():
    sevenlist = []
    for x in range(2000, 3201):
        if (x % 7 == 0) and not (x % 5 == 0):
            sevenlist.append(str(x))
    nofives = ", ".join(sevenlist)
    return nofives
