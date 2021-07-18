def lengthOfLongestSubstring( s: str) -> int:
    i = 0 
    longest = 0

    d = {}
    
    while i < len(s):
        count = 0 
        for j in range(i, len(s)):
            if s[j] not in d:
                d[s[j]] = 1
                count += 1
            else: 
                break
        d = {}
        if count > longest:
            longest = count
        
        
        i += 1

    print(longest)
    return longest
        

# 문자가 다른 가장 긴 부분문자열을 찾으래 ㅠㅡㅠ


lengthOfLongestSubstring("abcabcbb")