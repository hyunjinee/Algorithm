def reversing_words_slice(word):
    new_word = []
    words = word.split(' ')
    print(words)
    for word in words[::-1]:
        new_word.append(word)
    return " ".join(new_word)

if __name__ =="__main__":
    str1 = "파이썬 알고리즘은 정말 재미없다"
    str2 = reversing_words_slice(str1)
    print(str2)