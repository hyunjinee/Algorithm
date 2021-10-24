import sys
input  = sys.stdin.readline



N = int(input())

classes = [list(map(int, input().split())) for _ in range(N)]


cnt = [0] * N
for n in range(N):
    visited = [False for _ in range(N)]
    for grade in range(5):
        for student_id in range(N):
            if student_id != n and classes[student_id][grade] == classes[n][grade]:
                visited[student_id] = True
    print(visited)
    cnt[n] = len(list(filter(lambda x: x, visited)))

print(cnt.index(max(cnt)) + 1)

# students = [[0] * N for _ in range(N)]

# for i in range(5):
#     grade = []
#     for j in range(N):
#         grade.append(classes[j][i])
#     for j in range(len(grade)):
#         if grade.count(grade[j]) > 1:
#             for k in range(len(grade)) :
#                 if grade[j] == grade[k] and k!=j:
#                     students[j][k] = 1
# print(students)
# li = [sum(student) for student in students]
# max_value=  max(li)
# result = li.index(max_value) + 1
# print(result)
# # cnt = [ 0 ] * N

# for i in range(N):
#     count = 0
#     for j in range(N):
#         standard = classes[j][i]
#         if i == j : continue
#         if classes[i][j] : 

    
#     # for j in range(N):
    #     if i == j :
    #         continue
    #     if classes[i][j] 
    #     for k in range(5):
            