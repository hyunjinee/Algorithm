# 1287. Element Appearing More Than 25% In Sorted Array

![1287](https://user-images.githubusercontent.com/63354527/107140152-80e37080-6963-11eb-8254-c12e4afe05a0.PNG)

문제해석: 배열에서 25퍼센트이상 차지하는 숫자를 찾아서 반환해라..

## 풀이 1

객체를 하나만들고, 그 원소가 없으면 상태를 1로 해준다. 만약에 있으면 그 상태에 숫자 1을 더해준다. 그리고 만약 상태라 25퍼센트보다 많다면 그원소를 반환한다.

```javascript
var findSpecialInteger = function (arr) {
  let myObject = {};
  for (let i = 0; i < arr.length; i++) {
    if (!myObject[arr[i]]) {
      myObject[arr[i]] = 1;
    } else {
      myObject[arr[i]]++;
    }
  }

  for (let ele in myObject) {
    if (arr.length / 4 < myObject[ele]) return ele;
    // console.log(myObject[ele]);
    // console.log(ele);
  }
};
```

## 풀이 2

```javascript
const findSpecialInteger = (arr) => {
  if (arr.length == 1) return arr[0];

  const maxCount = arr.length / 4;
  let count = 1;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] == arr[i - 1]) {
      count++;
      if (count > maxCount) return arr[i];
    } else count = 1;
  }
};
```

## 풀이 3

```javascript
var findSpecialInteger = function (arr) {
  const twentyFivePercent = arr.length / 4;
  const map = {};

  for (const item of arr) {
    map[item] = map[item] + 1 || 1;
  }

  for (const key in map) {
    if (map[key] > twentyFivePercent) {
      return key;
    }
  }
};
```
