# First Unique Character in a String

![fis](https://user-images.githubusercontent.com/63354527/109472018-ed5e1500-7ab4-11eb-9e7a-cd1595f1f895.PNG)

# 풀이 1

의문이 들긴하지만 통과하긴했다.
다른 풀이도 좀 읽어봐야겠다.

```javascript
var firstUniqChar = function (s) {
  let myMap = new Map();

  for (let i = 0; i < s.length; i++) {
    if (myMap.has(s[i])) {
      let temp = myMap.get(s[i]);
      myMap.set(s[i], ++temp);
    } else {
      myMap.set(s[i], 1);
    }
  }
  console.log(myMap);

  for (let e of myMap) {
    if (e[1] == 1) return s.indexOf(e[0]);
  }
  return -1;
};
```

## 풀이 2

내 풀이랑 거의 비슷한거같긴하다.

```javascript
var firstUniqChar = function (s) {
  let map = {};

  for (let char of s) {
    map[char] ? map[char]++ : (map[char] = 1);
  }

  for (let i = 0; i < s.length; i++) {
    if (map[s[i]] === 1) return i;
  }

  return -1;
};
```

## 풀이 3

이거지!! 이게 풀이징
마지막 부터 인덱스를 세는 lastIndexOf도 기억해줘~~~~~~~~~~

```javascript
var firstUniqChar = function (s) {
  for (i = 0; i < s.length; i++)
    if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) return i;
  return -1;
};
```
