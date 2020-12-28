S = list(map(int, input().split()))
T = list(map(int, input().split()))

if sum(S) == sum(T):
    print(sum(S))
elif sum(S) > sum(T):
    print(sum(S))
else:
    print(sum(T))