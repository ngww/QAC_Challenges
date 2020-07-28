def name(string):
    lowerstring = string.lower()
    splitstring = lowerstring.split()
    substring = "am"
    
    count = splitstring.count(substring)

    return count