# 461. Hamming Distance

문제해석: hamming distance는 두개의 정수의 이진비트가 다른 것의 수이다.
hammingdistance를 리턴해라

## 풀이1

```javascript
var hammingDistance = function (x, y) {
  const arr = [];
  const arr1 = [];
  while (x >= 1) {
    if (x === 1) {
      arr.push(x);
      break;
    }
    let r = x % 2;
    arr.push(r);
    x = parseInt(x / 2);
  }
  while (y >= 1) {
    if (y === 1) {
      arr1.push(y);
      break;
    }

    let r1 = y % 2;
    arr1.push(r1);

    y = parseInt(y / 2);
  }
  arr.reverse();
  arr1.reverse();

  if (arr1.length === arr.length) {
    let count = 0;

    for (let k = 0; k < arr1.length; k++) {
      if (arr[k] !== arr1[k]) count++;
    }
    return count;
    return;
  }
  let maxlength = Math.max(arr.length, arr1.length);
  let whoisshort = arr.length > arr1.length ? arr1 : arr;
  let whoislong = arr.length < arr1.length ? arr1 : arr;
  let arr2 = new Array(maxlength);
  arr2.fill(0);
  console.log(arr2);
  console.log(whoisshort);
  for (let i = 0; i < arr2.length; i++) {
    arr2[arr2.length - 1 - i] = whoisshort[whoisshort.length - 1 - i] || 0;
  }
  let count = 0;
  console.log(arr2);
  for (let k = 0; k < arr2.length; k++) {
    if (whoislong[k] !== arr2[k]) count++;
  }
  return count;
};
```
