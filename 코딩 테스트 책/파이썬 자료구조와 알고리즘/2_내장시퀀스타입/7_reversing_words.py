def reversing_words(str1):
    words = str1.split(" ")
    rev_set = " ".join(reversed(words))
    return rev_set

def reversing_words2(str1):
    words = str1.split(" ")
    words.reverse()
    return " ".join(words)


#최종본
