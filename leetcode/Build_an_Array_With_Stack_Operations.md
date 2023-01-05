# 1441. Build an Array With Stack Operations

![1441](https://user-images.githubusercontent.com/63354527/107759132-3438d480-6d6b-11eb-8b08-c57588aeae96.PNG)

## 풀이 1

```javascript
var buildArray = function (target, n) {
  let list = [];
  let ans = [];

  for (let i = 1; i <= n; i++) list.push(i);

  let i = 0;
  let j = 0;
  let count = 0;
  while (count !== target.length) {
    if (target[i] == list[j]) {
      ans.push("Push");
      count++;
      i++;
      j++;
    } else if (target[i] != list[j]) {
      ans.push("Push");
      ans.push("Pop");

      j++;
    }
  }
  return ans;
};
```

## 풀이 2

```javascript
const buildArray = (target, n) => {
  const ret = [];
  for (let i = 0, j = 1; i < target.length; ++i, ++j) {
    ret.push("Push");
    target[i] !== j && ret.push("Pop") && --i;
  }
  return ret;
};
```
