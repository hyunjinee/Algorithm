from fractions import Fraction

#파이썬에서 숫자는 immutable 객체 타입 (불변객체타입)

def rounding_floats(number1, places):
    return round(number1, places)


def float_to_fractions(number):
    return Fraction(*number.as_integer_ratio())

def get_denominator(number1, number2):
    """분모를 반환한다"""
    a = Fraction(number1, number2)
    return a.denominator

def get_numerator(number1, number2):
    """분자를 반환한다."""
    a = Fraction(number1, number2)
    return a.numerator
def test_testing_floats():
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number6 = 6
    assert(rounding_floats(number1,number2) == 1.2)
    print(rounding_floats(number1, number2))
    print(rounding_floats(number1, 2))
    print(rounding_floats(number1,number2) == 1.2)
    assert(rounding_floats(number1*10, number3) ==10)
    assert(get_denominator(number2, number6) == number6)
    print(get_denominator(number2, number6))
    print(get_numerator(number2, number6))
    print("테스트완료욤^^")
if __name__ == "__main__":
    test_testing_floats()