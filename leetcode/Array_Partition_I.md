# 561. Array Partition I

![561](https://user-images.githubusercontent.com/63354527/107170065-bdb27480-6a02-11eb-8558-20fdb40e36c8.PNG)

문제 해석: 2n개를 n개의 쌍으로 나누고 그 쌍에서, 작은 값을 더해서 만들수 있는 가장 큰 값을 리턴해.

## 풀이 1

```javascript
var arrayPairSum = function (nums) {
  let ans = [];
  let temp = [];
  let length = nums.length;
  for (let i = 0; i < length; i++) {
    temp.push(Math.max(...nums));
    nums.splice(nums.indexOf(Math.max(...nums)), 1);

    if (temp.length == 2) {
      ans.push(Math.min(...temp));
      temp = [];
    }
  }
  return ans.reduce((a, x) => a + x);
};
```

## 풀이 2

```javascript
var arrayPairSum = function (nums) {
  nums.sort((a, b) => a - b);
  let result = 0;

  for (let i = 0; i < nums.length; i += 2) {
    result += nums[i];
  }

  return result;
};
```
