# 1572. Matrix Diagonal Sum

문제해석: matrix mat 가 주어질 것이다. 대각선의 합계를 반환해라.
첫번째 대각선의 합계에 쓴 숫자는 제외하고 두번째 대각선을 합해야된다.

## 풀이 1

대각선을 다더해주고 홀수인경우 가운데 값을 빼주었다!

```javascript
var diagonalSum = function (mat) {
  let sum = 0;
  let index = 0;
  for (let i = 0; i < mat.length; i++) {
    sum += mat[i][index];
    index++;
  }
  index = 0;
  for (let i = mat.length - 1; i >= 0; i--) {
    sum += mat[i][index];
    index++;
  }
  if (mat.length % 2 == 1) {
    console.log((1 + mat.length) / 2);
    console.log(mat[(1 + mat.length) / 2 - 1][(1 + mat.length) / 2] - 1);
    sum -= mat[(1 + mat.length) / 2 - 1][(1 + mat.length) / 2 - 1];
  }
  return sum;
};
```

## 풀이 2

인덱스가 같을 경우 한번만 더한다.

```javascript
var diagonalSum = function (mat) {
  let matLength = mat.length;
  let sum = 0;

  for (let i = 0, j = matLength - 1; i < matLength; i++, j--) {
    if (i === j) {
      sum += mat[i][j];
    } else {
      sum += mat[i][i] + mat[i][j];
    }
  }
  return sum;
};
```

## 풀이 3

코드 길이 단축

```javascript
let diagonalSum = function (mat) {
  let diagonal = 0;
  for (let i = 0, j = mat.length - 1; i < mat.length; i++, j--) {
    diagonal += i != j ? mat[i][i] + mat[i][j] : mat[i][j];
  }
  return diagonal;
};
```
