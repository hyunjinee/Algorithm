# 383. Ransom Note

![383](https://user-images.githubusercontent.com/63354527/106995447-468e9d80-67c2-11eb-8f3c-6ef0ddba52f5.PNG)

문제해석: magazine에 ransomNote있으면 true 없으면false

## 풀이 1

만약에 magazine에 ransomNote글자 있으면 그 글자를 없애버린다. 그리고 count 를 늘리고 만약에 글자를 다없애서 카운트가 ransomNote.length 와 같다면 true 다르면 false

```javascript
var canConstruct = function (ransomNote, magazine) {
  let count = 0;
  for (let i = 0; i < ransomNote.length; i++) {
    if (magazine.includes(ransomNote[i])) {
      magazine = magazine.replace(ransomNote[i], "");
      count++;
    }
  }
  return count == ransomNote.length;
};
```

## 풀이2

arr 로 바꾸고 arr가 다 감당할 수 있으면 true 다 감당못하고 index가 -1을 리턴하면 false

```javascript
var canConstruct = function (ransomNote, magazine) {
  const arr = magazine.split("");
  for (let i = 0; i < ransomNote.length; i++) {
    if (arr.indexOf(ransomNote[i]) === -1) {
      return false;
    } else {
      arr.splice(arr.indexOf(ransomNote[i]), 1);
    }
  }
  return true;
};
```
