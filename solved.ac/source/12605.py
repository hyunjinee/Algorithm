# 스페이스로띄어쓰기 된 단어들의 리스트주어질때 단어들을 반대 순서로 뒤집자.

# 각 라인은 w개의 영단어로 이루어져있으며, 총 L개의 알파벳을 가진다.

# w개의 영단어로 이룽져있고 L개의 알파벳

n = int(input())



for i in range(n):
    # 테스트 케이스 ㄱ ㅐ수

    arr = list(input().split(" "))
    arr.reverse()
    print(f'Case #{i+1}: ', end="")
    print(*arr)