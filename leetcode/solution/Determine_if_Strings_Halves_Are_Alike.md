# 1704. Determine if String Halves Are Alike

![1704](https://user-images.githubusercontent.com/63354527/106877947-b8141080-671c-11eb-8dea-d2e3bf840656.PNG)

문제해석: 짝수개의 문자로 이루어진 문자열이 주어진다. 이 문자열을 정확히 같은 길이로 쪼개고,a 를 첫번째꺼 b를 두번째꺼로 표현한다.
두개의 모음의 개수가 같으면 alike한 문자열이다. a와 b가 alike하면 true 아니면false 를 리턴
s는 대문자또는 소문자로 구성되어있다.

## 풀이 1

```javascript
var halvesAreAlike = function (s) {
  const vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
  let a = s.slice(0, s.length / 2);
  let b = s.slice(s.length / 2);

  let countA = 0;
  let countB = 0;
  for (let i = 0; i < a.length; i++) {
    if (vowels.includes(a[i])) {
      countA++;
    }
    if (vowels.includes(b[i])) {
      countB++;
    }
  }
  if (countA == countB) {
    return true;
  } else return false;
};
```

## 풀이2

match는 정규표현식과 일치하는 것의 배열을 리턴하니까 그 배열의 개수를 세어준다.

```javascript
var halvesAreAlike = function (s) {
  let len = s.length / 2;
  let count1 = (s.substring(0, len).match(/[AOEUIaeuoi]/g) || []).length;
  let count2 = (s.substring(len).match(/[AOEUIaeuoi]/g) || []).length;
  return count1 === count2;
};
```
