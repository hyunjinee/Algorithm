# 1122. Relative Sort Array

![1122](https://user-images.githubusercontent.com/63354527/107180621-6faa6a80-6a1c-11eb-9ec9-3e91fda672c6.PNG)

## 풀이 1

```javascript
var relativeSortArray = function (arr1, arr2) {
  let ans = [];
  for (let i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      let temp = arr1.splice(arr1.indexOf(arr2[i]), 1);
      ans.push(...temp);
    }
  }
  arr1.sort((a, b) => a - b);
  return [...ans, ...arr1];
};
```

## 풀이 2

```javascript
var relativeSortArray = (arr1, arr2) => {
  let map = new Map(),
    arr = [],
    notIncluded = [];
  for (const num of arr1) {
    if (map.has(num)) {
      map.set(num, map.get(num) + 1);
    } else {
      map.set(num, 1);
    }
  }
  for (const num of arr2) {
    let freq = map.get(num);
    while (freq) {
      arr.push(num);
      freq--;
    }
    map.delete(num);
  }
  for (let [key, val] of map) {
    while (val) {
      notIncluded.push(key);
      val--;
    }
  }
  return arr.concat(notIncluded.sort((a, b) => a - b));
};
```
