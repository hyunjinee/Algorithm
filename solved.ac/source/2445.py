N = int(input())

for i in range(1,N):
    print(i*"*"+(N-i)*" "*2+i*"*")
for i in range(1,N+1):
    print((N-i+1)*"*"+" "*(2*(i-1))+"*"*(N-i+1))