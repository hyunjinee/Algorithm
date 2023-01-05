# 1460. Make Two Arrays Equal by Reversing Sub-arrays

[문제 보러가기](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/)

## 🅰 설계

내부원소가 모두같으면 어떻게 하든 짤라서 붙일수 있지않을까..

## ✅ 후기

```js
var canBeEqual = function (target, arr) {
  target.sort((a, b) => a - b);
  arr.sort((a, b) => a - b);

  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (target[i] == arr[i]) count++;
  }

  if (count === arr.length) return true;
  else return false;
};
```

```js
var canBeEqual = function (arr, arr1) {
  const data = new Object();
  for (let i = 0; i < arr.length; ++i) {
    data[arr[i]] = data[arr[i]] + 1 || 1;
  }

  for (let i = 0; i < arr1.length; ++i) {
    if (data.hasOwnProperty(arr1[i]) === false) return false;
    if (data.hasOwnProperty(arr1[i]) === true) {
      if (data[arr1[i]] <= 0) return false;
      data[arr1[i]] = data[arr1[i]] - 1;
    }
  }
  return true;
};
```

```js
var canBeEqual = function (target, arr) {
  // if all numbers in target are present in arr, we can always make them equal
  let m1 = new Map(),
    m2 = new Map();
  target.forEach((num) => m1.set(num, m1.get(num) + 1 || 1));
  arr.forEach((num) => m2.set(num, m2.get(num) + 1 || 1));
  for (let num of arr) {
    if (m1.get(num) !== m2.get(num)) return false;
  }
  return true;
  // Time Complexity: O(n)
  // Space Complexity: O(n)
};
```

```js
var canBeEqual = function (target, arr) {
  const cmp = (a, b) => a - b;
  return target.sort(cmp).join("") === arr.sort(cmp).join("");
};
```

```js
var canBeEqual = function (target, arr) {
  return JSON.stringify(arr.sort()) === JSON.stringify(target.sort());
};
```

// 새롭게 알게되거나 공유해서 알게된 점

오랜만에 한방에풀어서조아쓰. 그냥 문제를 조금 다르게 해석할수 있는 능력이필요했다.

// 고생한 점

다양한 풀이를 읽고배웠어요.
