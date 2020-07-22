def alpha(sentence):
    words = sentence.split(" ")
    
    # " ".join() joins all the items in the list into a string
    # sorted() sorts the order of the items in the list
    # set() removes any copies of a word

    new_words = " ".join(sorted(set(words)))
    return new_words