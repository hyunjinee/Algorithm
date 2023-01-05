# 739. Daily Temperatures

![zz](https://user-images.githubusercontent.com/63354527/109627772-4f864b00-7b85-11eb-9357-78c7ede35e62.PNG)

## 풀이 1

```javascript
var dailyTemperatures = (T) =>
  T.map((t, i) => {
    let j = T.slice(i + 1).findIndex((a) => a > t);
    return j > -1 ? j + 1 : 0;
  });
```

## 풀이 2

```javascript
var dailyTemperatures = function (T) {
  const stack = [];

  T.forEach((temperature, index) => {
    while (stack.length && T[stack[stack.length - 1]] < temperature) {
      const toBeReplacedIndex = stack.pop();
      T[toBeReplacedIndex] = index - toBeReplacedIndex; // replace with index inplace
    }
    stack.push(index);
  });

  while (stack.length) {
    T[stack.pop()] = 0;
  }

  return T;
};
```

```javascript
var dailyTemperatures = function (T) {
  let stack = [],
    res = Array(T.length).fill(0);
  for (let i = 0; i < T.length; i++) {
    while (stack.length > 0 && T[stack[stack.length - 1]] < T[i]) {
      let idx = stack.pop();
      res[idx] = i - idx;
    }
    stack.push(i);
  }
  return res;
};
```
