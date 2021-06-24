n = int(input())
alpa =dict()
alpa['A'] = 0
alpa['B'] = 1
alpa['C'] = 2
alpa['D'] = 3
alpa['E'] = 4
alpa['F'] = 5
alpa['G'] = 6
alpa['H'] = 7
alpa['I'] = 8
alpa['J'] = 9
alpa['K'] = 10
alpa['L'] = 11
alpa['M'] = 12
alpa['N'] = 13
alpa['O'] = 14
alpa['P'] = 15
alpa['Q'] = 16
alpa['R'] = 17
alpa['S'] = 18
alpa['T'] = 19
alpa['U'] = 20
alpa['V'] = 21
alpa['W'] = 22
alpa['X'] = 23
alpa['Y'] = 24
alpa['Z'] = 25

for i in range(n):

    num = input()

    total = alpa[num[0]] * 26**2 + alpa[num[1]] * 26 + alpa[num[2]]

    num = int(num[4:]) -total

    if -100<= num <= 100:
        print("nice")
    else: print("not nice")

