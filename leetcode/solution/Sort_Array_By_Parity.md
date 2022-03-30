# 905. Sort Array By Parity

![905](https://user-images.githubusercontent.com/63354527/106888168-8786a380-6729-11eb-9021-1d7ed0d40334.PNG)

문제해석: 양의 정수로 이루어진 배열A가 주어진다. 짝수 앞에다 높고 홀수는 뒤에다놓은 배열을 리턴해라 너는 이런식의 배열은 어떤것이든 반환해도 좋다.

앞에 짝수고 뒤에 홀수면 순서는 상관없다는 뜻 같다.

## 풀이1

짝수면 arr 홀수면 arr1에넣고 concat

```javascript
var sortArrayByParity = function (A) {
  let arr = [];
  let arr1 = [];
  for (let i = 0; i < A.length; i++) {
    if (A[i] % 2 == 0) {
      arr.push(A[i]);
    } else arr1.push(A[i]);
  }
  const ans = arr.concat(arr1);
  console.log(ans);
};

sortArrayByParity([3, 1, 2, 4]);
```

## 풀이2

descirption 읽다가.. 요런 풀이도 있구나..

```javascript
var sortArrayByParity = function (A) {
  let left = 0,
    right = A.length - 1,
    temp;

  // swap when there is odd integer in left side and even integer in right side
  while (left < right) {
    while (A[left] % 2 === 0) {
      ++left;
    }
    while (A[right] % 2 === 1) {
      --right;
    }
    if (left < right) {
      temp = A[left];
      A[left] = A[right];
      A[right] = temp;
      ++left;
      --right;
    }
  }
  return A;
};
```
