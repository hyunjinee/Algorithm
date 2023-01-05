# Remove Palindromic Subsequences

![palin](https://user-images.githubusercontent.com/63354527/110419806-5eb54d80-80dd-11eb-9ab8-94bf2d709c05.PNG)

## 풀이 1

2글자니까 무조건 2번으로는 다지울 수 있고 경우의 수는 0,1,2세가지 밖에 없다.

```javascript
var removePalindromeSub = function (S) {
  if (!S) return 0;
  for (let i = 0, j = S.length - 1; i < j; i++, j--)
    if (S.charAt(i) !== S.charAt(j)) return 2;
  return 1;
};
```
