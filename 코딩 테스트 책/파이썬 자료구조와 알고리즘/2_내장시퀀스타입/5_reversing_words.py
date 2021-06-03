def reverse_words_brute(string):
    word, sentence = [], []
    for character in string:
        if character != " ":
            word.append(character)
        else:
            if word:
                sentence.append("".join(word))
            word = []
    if word != "":
        sentence.append("".join(word))
    sentence.reverse()
    return " ".join(sentence)
if __name__  == "__main__":
    str1 = "파이썬 알고리즘은 정말 재미없다"
    str2 = reverse_words_brute(str1)
    print(str2)   