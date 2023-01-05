# 1299. Replace Elements with Greatest Element on Right Side

![dd](https://user-images.githubusercontent.com/63354527/108309129-55c70f80-71f4-11eb-9c38-c468844ed0c9.PNG)

## 풀이 1

```javascript
var replaceElements = function (arr) {
  for (let i = 0; i < arr.length; i++) {
    arr[i] = Math.max(...arr.slice(i + 1));
  }
  arr[arr.length - 1] = -1;
  return arr;
};
```

## 풀이 2

```javascript
const replaceElements = (arr) => {
  const result = new Array(arr.length);
  result[arr.length - 1] = -1;

  for (let i = arr.length - 1; i > 0; i -= 1) {
    result[i - 1] = Math.max(arr[i], result[i]);
  }

  return result;
};
```
