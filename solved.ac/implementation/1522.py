def solution():
    A = input()

    a_count = A.count('a')
    answer = len(A)

    for i in range(0, len(A) - a_count + 1):
        answer = min(A[i:i+a_count].count('b'), answer)
    
    for i in range(1, a_count):
        answer = min(A[len(A) - i: len(A)].count('b') +  A[0:a_count - i].count('b'), answer)

    print(answer)   

solution()