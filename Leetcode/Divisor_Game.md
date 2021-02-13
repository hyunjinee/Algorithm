# 1025. Divisor Game

![1025](https://user-images.githubusercontent.com/63354527/107840804-2c277600-6df9-11eb-8482-7c72b87001e6.PNG)

## 풀이 1

자신이 무조건 짝수를 갖고있으면 이긴다.

```javascript
var divisorGame = function (N) {
  return N % 2 === 0;
};
```
