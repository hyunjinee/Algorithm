# Climbing Stairs

![climb](https://user-images.githubusercontent.com/63354527/109474057-70806a80-7ab7-11eb-8fef-f9fbf6cfa220.PNG)

## 풀이 1

될수 있는 경우의 수를 카운트에 더해주고 겹치는 부분은 팩토리얼 계산으로 나눠주었다.

```javascript
var climbStairs = function (n) {
  let ministep = 1;
  let bigstep = 2;
  let count = 0;
  for (let i = 0; i <= n / 1; i++) {
    for (let j = 0; j <= n / 2; j++) {
      //   console.log(i, j);
      if (1 * i + 2 * j == n) {
        let temp = fac(i + j) / fac(i) / fac(j);
        count += temp;
      }
    }
  }
  return count;
};
function fac(n) {
  if (n == 1 || n == 0) return 1;
  return n * fac(n - 1);
}
```

## 풀이 2

```javascript
var climbStairs = function (n) {
  let prev = 0;
  let cur = 1;
  let temp;

  for (let i = 0; i < n; i++) {
    temp = prev;
    prev = cur;
    cur += temp;
  }
  return cur;
};
```

```javascript
var climbStairs = function (n) {
  // dp[i] represents # of ways to reach i-th floor
  let dp = new Array(n + 1); // size is n+1 because array is zero-indexed
  (dp[0] = 1), (dp[1] = 1);
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
  // Time Complexity: O(N)
  // Space Complexity: O(N)
};
```
