import sys
from collections import deque
from collections import Counter

# 테스트케이스 입력 받은 만큼 반복
for _ in range(int(sys.stdin.readline())):
    try:						# 에러를 잡기 위한 try-except
        p = sys.stdin.readline()			# 명령어 입력
        n = int(sys.stdin.readline())			# 배열 원소 수
        arr = sys.stdin.readline()[1:-2]		# 배열 입력. 앞뒤의 [] 및 맨 마지막 \n 제거.
        if len(arr) > 0:				# arr이 비어있지 않다면 
            arr = deque(map(int, arr.split(',')))	# , 로 구분하여 큐로 변환
        else:						# arr가 비었다면
            arr = deque(arr)				# 그 상태로 큐료 변환

        isAsc = True					# R 추적. 

	# D의 개수를 n과 비교하여 n보다 많으면 에러 생성, 같으면 [] 출력 후 다음으로 넘김
        if 'D' in p:					
            num_p = Counter(p).get('D')
            if num_p > n:
                raise ValueError
            elif num_p == n:
                print("[]")
                continue

        for cmd in p:					# 각 명령어마다 순서대로 실행
            if cmd == 'R':				# R이면 isAsc만 변경
                isAsc = not isAsc
            if cmd == 'D':				# D이면 isAsc의 값에 따라 pop 또는 popleft
                if isAsc:
                    arr.popleft()
                else:
                    arr.pop()
        else:						# for문이 끝난 후
            if not isAsc:				# isAsc가 false이면 arr 뒤집음
                arr.reverse()
            print(str(list(arr)).replace(' ', ''))	# arr을 문자열로 변환, 공백 제거 후 출력
    except:						# 에러 발견 시 'error' 출력
        print("error")