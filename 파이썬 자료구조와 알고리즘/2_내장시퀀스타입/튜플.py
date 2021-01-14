#튜플은 쉼표로 구분된 값으로 이루어지는 불변 시퀀스 타입

t1 = 1234, '안녕'
print(t1[1])
print(t1)

t2 = t1, (1,2,3,4,5)
print(t2)


empty = ()
t1 = "안녕",
print(t1)
t2 = ('안녕')
print(t2)


t = 1,5,7,8,9,4,1,4

print(t.count(4))

t =  1,5,7

print(t.index(5))


x, *y = (1,2,3,4)
print(x)
print(y)


