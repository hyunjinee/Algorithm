# 가변 mutable 객체 타입

# 파이썬에서 튜플 문자열 바이트는 불변객체타입이며, 리스트와 바이트는 가변객체타입니다.
# 일반적으로 불변객체 타입은 가변 객체 타입보다 효율적이다. 


# 파이썬의 모든 변수는 객체 참조이므로 가변 객체를 복사할 때는 매우 주의해야한다.
# a = b 라 할때 , a 가 실제 b가 가르키는 곳을 가르킨다.

# 깊은 복사의 예
myList = [1,2,3,4]
newList = myList[:]
newList2 = list(myList)
print(newList)
print(newList2)
myList.append(5)
print(myList)
print(newList)
print(newList2)

# 셋에서 깊은 복사의 예

people = {"버피", "에인절", "자일스"}
slayers = people.copy()
slayers.discard("자일스")
slayers.remove("에인절")
print(slayers)
print(people)

# 딕셔너리의 깊은 복사 예제
myDict = {"안녕":"세상"}
newDict = myDict.copy()

# 기타 깊은 복사를 할때는 copy 모듈을 사용

import copy
myObj = "다른 어떤 객체"
newObj = copy.copy(myObj) # 얕은 복사
newObj2 = copy.deepcopy(myObj) # 깊은 복사
print(myObj)
newObj = "바뀜"
newObj2 = "바뀜"
print(myObj)