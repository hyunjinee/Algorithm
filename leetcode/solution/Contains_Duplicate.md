# Contains Duplicate

![contains](https://user-images.githubusercontent.com/63354527/109468405-de289880-7aaf-11eb-856b-f52e92803f14.PNG)

## 풀이 1

맵을 이용해보았다.

```javascript
var containsDuplicate = function (nums) {
  let myMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (myMap.has(nums[i])) {
      return true;
    } else {
      myMap.set(nums[i], 0);
    }
  }
  return false;
};
```

## 풀이 2

set의 크기가 더 작다면 true 더 크다면 false

```javascript
var containsDuplicate = function (nums) {
  return new Set(nums).size < nums.length;
};
```

## 풀이 3

어떠한 것이라도 한번이라도 겹치면 true

```javascript
var containsDuplicate = function (nums) {
  return nums.sort().some((a, i) => a === nums[i - 1]);
};
```
