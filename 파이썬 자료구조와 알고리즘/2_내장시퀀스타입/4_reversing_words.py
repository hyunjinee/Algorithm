def reverser(string1, p1=0, p2=None):
    if len(string1) <2:
        return string1
    p2 = p2 or len(string1)-1
    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1+=1
        p2-=1

def reversing_words_sentence_logic(string1):
    reverser(string1)
    p = 0
    #print(string1)
    start = 0
    while p < len(string1):
        if string1[p] == u"\u0020":
            reverser(string1, start, p-1)
            start = p + 1
        p+=1
    reverser(string1, start, p-1)
    return "".join(string1)


if __name__  == "__main__":
    str1 = "파이썬 알고리즘은 정말 재미없다"
    str2 = reversing_words_sentence_logic(list(str1))
    print(str2)