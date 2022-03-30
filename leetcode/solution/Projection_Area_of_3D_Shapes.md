# 883. Projection Area of 3D Shapes

![883](https://user-images.githubusercontent.com/63354527/110294852-be571e80-8033-11eb-9631-f7528150e89c.PNG)

## 풀이 1

```javascript
var projectionArea = function (grid) {
  let res = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] > 0) res++;
    }
    res += Math.max(...grid[i]);
    res += Math.max(...grid.map((r) => r[i]));
  }
  return res;
};
```

## 풀이 2

```javascript
var projectionArea = function (grid) {
  const x = grid.reduce((a, b) => a.concat(b), []).filter((x) => x > 0).length;
  const y = grid.map((r) => Math.max(...r)).reduce((acc, idx) => acc + idx);
  const z = grid[0]
    .map((_, i) => Math.max(...grid.map((r) => r[i])))
    .reduce((acc, idx) => acc + idx);
  return x + y + z;
};
```

## 풀이 3

```javascript
var projectionArea = function (grid) {
  return [
    ...grid
      .reduce((a, b) => a.concat(b), [])
      .filter((x) => x > 0)
      .map((_) => 1),
    ...grid.map((r) => Math.max(...r)),
    ...grid[0].map((_, i) => Math.max(...grid.map((r) => r[i]))),
  ].reduce((acc, idx) => acc + idx);
};
```
