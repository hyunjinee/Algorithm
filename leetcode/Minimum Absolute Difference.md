
# 1200. Minimum Absolute Difference

[문제 보러가기](https://leetcode.com/problems/minimum-absolute-difference/)

## 🅰 설계
일단 최소한 작은 절댓값을 찾아야한다 모두 정수고 다른숫자이므로 가장작은 값은 1이상이겠지?

```js
var minimumAbsDifference = function(arr) {
  const ans = [];
  arr.sort((a, b) => a - b);
  let minDiff = Infinity;
  for (let i = 1; i < arr.length; i++) {
    minDiff = Math.min(minDiff, arr[i] - arr[i - 1]);
  }
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] - arr[i - 1] === minDiff) ans.push([arr[i - 1], arr[i]]);
  }
  return ans;
};
```

```js
const minimumAbsDifference = arr => {
  const RANGE = 10 ** 6;
  const data = new Int8Array(RANGE * 2 + 1);
  let min = arr[0];
  let max = arr[0];
  for (let i = 0; i < arr.length; ++i) {
    data[arr[i] + RANGE] = 1;
    if (arr[i] < min) min = arr[i];
    if (arr[i] > max) max = arr[i];
  }
  let ret = [];
  let diff = max - min;
  let prev = min + RANGE;
  for (let i = prev + 1; i <= max + RANGE; ++i) {
    if (data[i] === 0) continue;
    if (i - prev === diff) {
      ret.push([prev - RANGE, i - RANGE]);
    } else if (i - prev < diff) {
      diff = i - prev;
      ret = [[prev - RANGE, i - RANGE]];
    }
    prev = i;
  }
  return ret;
};
```

```js
var minimumAbsDifference = function(arr) {
    arr.sort((a, b) => a - b);
	
    const map = {};
    let abs, min = Infinity;

    for (let i = 1; i < arr.length; i++) {
        abs = Math.abs(arr[i - 1] - arr[i]);
        if (abs < min) min = abs; // keep track of min abs

        // keep track of all abs diff
        if (!map[abs]) map[abs] = [];
        map[abs].push([arr[i - 1], arr[i]]);
    }

    return map[min];
};
```
## ✅ 후기
// 새롭게 알게되거나 공유해서 알게된 점

음.. 후기는없다..


// 고생한 점
