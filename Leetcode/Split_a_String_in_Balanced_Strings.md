# 1221. Split a String in Balanced Strings

해석: 균형잡힌 문자열이란L과 R의 문자의 개수가 같은 것을 말한다.
균형잡힌 문자열 s 가 주어진다. 이것을 쪼개서 가장많은 균형잡힌 문자열을 만들어라.
그리고 반환해라 가장 많은 양의 쪼개진 균형잡힌 문자열의 개수를!!!

풀이1

```javascript
var balancedStringSplit = function (s) {
  let plus = 1;
  let minus = -1;
  let i = 0;
  let sum = 0;
  let count = 0;
  while (i < s.length) {
    if (s[i] == "R") {
      sum = sum + plus;
    } else {
      sum = sum + minus;
    }
    if (sum == 0) {
      count++;
    }
    i++;
  }
  return count;
};
```

풀이2

```javascript
var balancedStringSplit = function (s) {
  var numberOfR = 0,
    numberOfL = 0,
    numberOfBalancedStr = 0;
  for (var x of s) {
    x === "L" ? numberOfL++ : numberOfR++;
    if (numberOfL === numberOfR) {
      numberOfBalancedStr++;
      (numberOfL = 0), (numberOfR = 0);
    }
  }
  return numberOfBalancedStr;
};
```

풀이3

```javascript
var balancedStringSplit = function (s) {
  let val = 0,
    res = 0;
  for (let x of s) {
    x === "R" ? val++ : val--;
    if (val == 0) res++;
  }
  return res;
};
```

풀이4

```javascript
var balancedStringSplit = function (s) {
  let ans = 0;

  s.split("").reduce((acc, cur) => {
    acc += cur == "R" ? 1 : -1;
    ans += acc == 0 ? 1 : 0;
    return acc;
  }, 0);

  return ans;
};
```
