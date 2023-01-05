# The K Weakest Rows in a Matrix

![k](https://user-images.githubusercontent.com/63354527/108716662-c0af7800-755f-11eb-9ddd-1892ef0a813a.PNG)

## 풀이 1

좀더 나은 풀이를 쓰고싶은 마음은 굴뚝같아

```javascript
var kWeakestRows = function (mat, k) {
  let soilders = {};

  for (let i = 0; i < mat.length; i++) {
    let count = 0;
    for (let j = 0; j < mat[0].length; j++) {
      if (mat[i][j]) count++;
    }
    soilders[i] = count;
  }

  let ans = [];
  let temp = [];
  for (let soilder in soilders) {
    temp.push(soilders[soilder]);
  }

  while (ans.length !== k) {
    console.log(ans.length);
    let min = Math.min(...temp);
    temp.splice(temp.indexOf(min), 1);
    for (let soilder in soilders) {
      if (ans.length == k) break;
      if (soilders[soilder] === min) {
        ans.push(+soilder);
        delete soilders[soilder];
      }
    }
  }
  return ans;
};
```

## 풀이 2

진짜 진심으로 개쩐다.

```javascript
var kWeakestRows = function (mat, k) {
  return mat
    .map((e, index) => {
      return { index: index, strongness: numOfsoldiers(e) };
    })
    .sort((r1, r2) => {
      let eq = r1.strongness - r2.strongness;
      return eq == 0 ? r1.index - r2.index : eq;
    })
    .slice(0, k)
    .map((e) => e.index);
};

var numOfsoldiers = function (row) {
  let i = 0;
  while (row[i] != 0 && i <= row.length - 1) i++;
  return i;
};
```

## 풀이 3

```javascript
var kWeakestRows = function (M, K) {
  let y = M.length,
    x = M[0].length,
    vis = new Uint8Array(y),
    ans = [];
  for (let j = 0; j <= x; j++)
    for (let i = 0; i < y; i++) {
      if (!vis[i] && !M[i][j]) ans.push(i), vis[i]++;
      if (ans.length === K) return ans;
    }
};
```
