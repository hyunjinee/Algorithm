# 1002. Find Common Characters

![000](https://user-images.githubusercontent.com/63354527/108047989-d6b5c800-7089-11eb-8259-e5f9fdb0e12a.PNG)

## 풀이 1

```javascript
var commonChars = function (A) {
  let ans = [];
  for (let i = 0; i < A[0].length; i++) {
    let count = 0;
    for (let j = 1; j < A.length; j++) {
      if (A[j].includes(A[0][i])) {
        count++;
        A[j] = A[j].replace(A[0][i], "");
      }
    }
    if (count == A.length - 1) ans.push(A[0][i]);
  }
  return ans;
};
```

## 풀이 2

```javascript
var commonChars = function (A) {
  let res = [...A[0]];
  for (let i = 1; i < A.length; i++) {
    res = res.filter((c) => {
      const l = A[i].length;
      A[i] = A[i].replace(c, "");
      return l > A[i].length;
    });
  }
  return res;
};
```

## 풀이 3

```javascript
var commonChars = function (A) {
  let ans = A[0].split("");
  for (let i = 1; i < A.length; i++) {
    ans = findCommon(ans, A[i].split(""));
  }
  return ans;
};

var findCommon = function (a, b) {
  return a.filter((v) => {
    let i = b.indexOf(v);
    if (i !== -1) {
      b.splice(i, 1);
      return true;
    }
    return false;
  });
};
```
