# 파이썬은 불변의 str 타입을 사용하여 문자열을 표현한다. 문자열이란 곧 일련의 문자이다.
# 파이썬의 모든 객체에는 두가지 출력 형식이 있다.
# 문자열 형식은사람을 위해서 설계되었고, 표현 형식은 파이썬 인터프리터에서 사용하는문자열로 보통 디버깅할때 사용
# 파이썬 클래스를 작성할 때에는 문자열 표현을 정의하는 것이 중요

slayer = ["버피" , "앤" , "아스틴"]
print("".join(slayer))
print("-<>-".join(slayer))
print("".join(reversed(slayer)))

name = "이현진"
print(name.ljust(50, "-"))
print(name.rjust(50, "-"))

import decimal

print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9")))

hero = "버피"
number = 999
print("{number}: {hero}".format(**locals()))

slayer = "로미오\n줄리엣"
print(slayer.splitlines())

slayers = "버피*크리스-메리*16"
fields =slayers.split("*")
print(fields)
job = fields[1].split("-")
print(job)


def erase_space_from_string(string):
    s1 = string.split(" ")
    s2 = "".join(s1)
    return s2

start = "안녕*세상*!"
print(start.split("*"))
print(start.split("*",1))
print(start.rsplit('*',1))


slayers = "로미오 & 줄리엣999"
print(slayers.strip("999"))


slayers = "Buffy and Faith"
print(slayers.swapcase())
