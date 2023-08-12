word = input()


for i in range(len(word)//10+1):
    if len(word)//10 >0 :
        print(word[:10])
        word = word[10:]
    else:
        print(word)