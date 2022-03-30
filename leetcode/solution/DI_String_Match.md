# 942. DI String Match

![942](https://user-images.githubusercontent.com/63354527/107741795-32621780-6d51-11eb-8bd6-227c8d780766.PNG)

일단 처음에 어떻게 해야되는지를 모르겠다.
어떠한 순열도 반환해도되는게 중요한것 같은데..

결국엔 decrese할 때는 가장 큰것부터 내려오고 increse할때는 작은것 부터 올라가면 된다.

## 풀이 1

```javascript
const diStringMatch = (S) => {
  let num = [];
  let inc = 0;
  let dec = S.length;
  let i = 0;
  while (num.length !== S.length + 1) {
    num[i] = S[i] === "D" ? dec-- : inc++;
    i++;
  }

  console.log(inc);
  return num;
};
```

진짜 개멋있다..

## 풀이 2

```javascript
var diStringMatch = function (S) {
  let res = [],
    low = 0,
    high = S.length;
  for (let i = 0; i <= S.length; i++) {
    if (S.charAt(i) == "I") {
      res.push(low++);
    } else {
      res.push(high--);
    }
  }
  return res;
};
```
