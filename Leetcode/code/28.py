def strStr(haystack: str, needle: str) -> int:
    # 들어있으면 인덱스를 리턴하고 
    if needle in haystack:

        print(haystack.index(needle))

    else: return -1

strStr("hello", "ll")
    # 들어있지 않으면 -1 을 리턴하는 것
    
