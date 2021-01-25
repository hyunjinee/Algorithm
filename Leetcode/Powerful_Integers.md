# 970. PowerFul Integers

양수 x랑 y 가 있다.근데이게 파워풀 정수가 되려면 위에 조건을 만족해야하고, 우리는 그 파워풀 정수들을 리턴해야돼.
bound 보다 작거나 같은!!!
순서없이 리턴해도되고, 각각의 값은 적어도 한번 발생해야된다.

## 풀이

```javascript
let powerfulIntegers = function (x, y, bound) {
  let answer = new Set();

  for (let i = 0; i < 20; i++) {
    for (let j = 0; j < 20; j++) {
      let P_I = Math.pow(x, i) + Math.pow(y, j);
      if (P_I <= bound) {
        answer.add(P_I);
      }
    }
  }

  return Array.from(answer);
};
```

결국 관건은 시간이 문제였다. 저기 i, j 를 컨트롤 하려고했는데 일단 그냥 어림잡아서 100으로 놓았을 때 모든 테스트 케이스를 통과했다.
그런데 계산기로 2의 20승이 10의 6승을 조금 넘는 것을 알아냈고,조금 수정했다.

## 풀이2

```javascript
let powerfulIntegers = function (x, y, bound) {
  const res = [];

  for (let i = 0; i < 20; i++) {
    for (let j = 0; j < 20; j++) {
      if (x ** i + y ** j <= bound) {
        res.push(x ** i + y ** j);
      }
    }
  }

  return [...new Set(res)];
};
```

## 풀이3

```javascript
var powerfulIntegers = function (x, y, bound) {
  const ans = new Set();
  for (let i = 0; (i < 20) & (Math.pow(x, i) <= bound); i++) {
    for (let j = 0; (j < 20) & (Math.pow(y, j) <= bound); j++) {
      const v = Math.pow(x, i) + Math.pow(y, j);
      if (v <= bound) ans.add(v);
    }
  }
  return Array.from(ans);
};
```
