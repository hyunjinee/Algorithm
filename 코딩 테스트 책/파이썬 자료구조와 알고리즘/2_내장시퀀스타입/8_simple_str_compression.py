def str_compression(s):
    count, last = 1, ""
    list_aux = []
    for i ,c in enumerate(s):
        if last == c:
            count +=1
        else:
            if i!=0:
                list_aux.append(str(count))
            list_aux.append(c)
            count =1
            last = c
        list_aux.append(str(count))
        return "".join(list_aux)
if __name__ == "__main__" :
    result = str_compression("aabcccccaaa")
    print(result)