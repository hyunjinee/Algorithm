
# JadenCase 문자열 만들기
[문제 보러가기](https://programmers.co.kr/learn/courses/30/lessons/12951)

## 🅰 설계
```py
def solution(s):
    s = s.lower()
    L=s.split(" ")
    answer = ""
    for i in L:
        i= i.capitalize()
        answer+= i+" "
    return answer[:-1]
```

> js

```js

function solution(s) {
    return s.split(" ").map(v => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase()).join(" ");
}
```

## ✅ 후기
// 새롭게 알게되거나 공유해서 알게된 점
// 고생한 점
