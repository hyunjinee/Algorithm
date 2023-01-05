# 1716. Calculate Money in Leetcode Bank

![1716](https://user-images.githubusercontent.com/63354527/108439154-12bc7900-7294-11eb-9ae2-4da09caebf06.PNG)

## 풀이 1

```javascript
var totalMoney = function (n) {
  let 몫 = parseInt(n / 7);
  console.log(몫);
  let sum = 0;
  for (let i = 0, j = 4; i < 몫; i++, j++) {
    sum += j * 7;
  }
  let 나머지 = n % 7;
  console.log(나머지);
  sum = sum + ((나머지 + 1) * 나머지) / 2 + 나머지 * 몫;
  return sum;
};
```

## 풀이 2

```javascript
var totalMoney = function (n) {
  let weeks = Math.floor(n / 7);
  let res = 0;
  for (let i = 1; i <= weeks; i++) {
    res += 7 * (i + 3);
  }
  for (let i = 7 * weeks; i < n; i++) {
    res += ++weeks;
    console.log(weeks);
  }
  return res;
};
```
