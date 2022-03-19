# 205. Isomorphic_Strings
![is](https://user-images.githubusercontent.com/63354527/105789785-6655e280-5fc6-11eb-8e41-08906dc6a68c.PNG)


해석: s랑t를 줄께, 이소모르픽 문자열인지 판단해봐
문자가 대체될수 있을 때 이소모르픽이다.
모든 발생은 무조건 바뀌어야한다. 다른 문자와 함께, 다른 문자들은 보존하면서.

## 풀이

```javascript
var isIsomorphic = function (s, t) {
  if (s.length != t.length) return false;
  let m = new Map();
  for (let i = 0; i < s.length; i++) {
    if (!m.has(s[i])) m.set(s[i], t[i]);
    else {
      if (m.get(s[i]) != t[i]) {
        return false;
      }
    }
  }
  return new Set([...m.values()]).size == m.size;
};
```
