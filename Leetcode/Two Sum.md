# 1. Two Sum

[문제 보러가기](https://leetcode.com/problems/two-sum/)

## 🅰 설계

리트코드 1번문제다.ㅋㅋㅋㅋ
두개더해가지구 타겟을 만들어랏!!!

## ✅ 후기

```js
var twoSum = function (nums, target) {
  let ans;
  let ans1;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        ans = i;
        ans1 = j;
      }
    }
  }
  console.log(ans, ans1);
  return [ans, ans1];
};
```

```js
var twoSum = function (nums, target) {
  let map = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (map.has(target - nums[i])) {
      return [map.get(target - nums[i]), i];
    } else {
      map.set(nums[i], i);
    }
  }
  return [];
};
```

```js
var twoSum = function (nums, target) {
  let hash = {};

  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    if (hash[target - n] !== undefined) {
      return [hash[target - n], i];
    }
    hash[n] = i;
  }
  return [];
};
```

// 새롭게 알게되거나 공유해서 알게된 점
// 고생한 점
