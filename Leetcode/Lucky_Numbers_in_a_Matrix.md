# 1380. Lucky Numbers in a Matrix

![1380](https://user-images.githubusercontent.com/63354527/108051656-7c6b3600-708e-11eb-9d78-059e7dee5ca8.PNG)

## 풀이 1

```javascript
var luckyNumbers = function (matrix) {
  let minimums = [];
  for (let i = 0; i < matrix.length; i++) {
    let m = Math.min(...matrix[i]);
    let index = matrix[i].indexOf(m);
    minimums.push(m, index);
  }

  for (let j = 0; j < minimums.length; j += 2) {
    let count = 0;
    for (let k = 0; k < matrix.length; k++) {
      if (matrix[k][minimums[j + 1]] <= minimums[j]) count++;
    }
    if (count == matrix.length) {
      return [minimums[j]];
      // console.log([minimums[j]]);
    }
  }
  return [];
};
```

## 풀이 2

```javascript
var luckyNumbers = function (matrix) {
  var min = matrix.map((x) => Math.min(...x));
  var max = matrix[0].map((_, i) => Math.max(...matrix.map((x) => x[i])));
  return min.filter((x) => max.includes(x));
};
```
