
people = ["버피", "페이스"]
people.append("현진")
print(people)
people[len(people):] = ["흐흐"]
print(people)



people = ["버피", "페이스"]

people.extend("자일스")
print(people)
people+="윌로"
print(people)
people +=["젠더"]
print(people)

a = [-1,4,5,8,10]

del a[0]
print(a)

del a[2:3]
print(a)
# del a
# print(a)

#객체 참조가 삭제되고 다른 객체가 더이상 그데이터를 참조하지 않을때 파이썬은 그 데이터 항목을 가비지 컬렉터에 수집한다.

#리스트 언패킹

first , *rest = [1,2,3,4,5]
print(first)
print(rest)

# list comprehension

a = [y for y in range(1900, 1940) if y%4 ==0]
print(a)