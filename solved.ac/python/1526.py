from sys import stdin

N = int(stdin.readline())


while True:

    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        print(N)

        break

    N -= 1