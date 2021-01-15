from collections import Counter
#애너그램은 문장또는 단어의 철자 순서를 바꾸는 놀이다!
def is_anagram(s1, s2):
    counter = Counter()
    print(counter)
    for c in s1:
        counter[c] +=1
    for c in s2:
        counter[c] -=1
    for i in counter.values():
        if i: 
            return False
    return True

def test_is_anagram():
    s1 = "marina"
    s2 = "aniram"
    assert(is_anagram(s1,s2) is True)
    s1 = "google"
    s2 = "gouglo"
    assert(is_anagram(s1, s2) is False)
    print("테스트 토오오오옹과")


test_is_anagram()