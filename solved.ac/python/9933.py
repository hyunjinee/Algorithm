n = int(input())


lst = list()

for i in range(n):

    string = input()

    lst.append(string)
    if string == string[::-1]:
        print(len(string) , string[len(string)//2])
        break
    if string[::-1] in lst:
        print(len(string) , string[len(string)//2])