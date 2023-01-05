# 657. Robot Return to Origin

![657](https://user-images.githubusercontent.com/63354527/108309361-c0784b00-71f4-11eb-9d24-ea8da0cbf34c.PNG)

## 풀이 1

객체로 상태를 관리해주고 방향에 따라서 if문을 작성해서 결론을 내었다.

```javascript
var judgeCircle = function (moves) {
  let move = {
    x: 0,
    y: 0,
  };

  for (let i = 0; i < moves.length; i++) {
    if (moves[i] == "R") {
      move.x++;
    } else if (moves[i] == "L") {
      move.x--;
    } else if (moves[i] == "U") {
      move.y++;
    } else {
      move.y--;
    }
  }
  if (move.x == 0 && move.y == 0) return true;
  else return false;
};
```

객체로 관리할 필요없었고, switch문으로 좀 다르게 그리고 마지막 boolean값 반환할때도 더 쉽게 가능하다.

## 풀이2

```javascript
var judgeCircle = function (moves) {
  let x = 0,
    y = 0;
  for (i = 0; i < moves.length; i++) {
    switch (moves[i]) {
      case "R":
        x++;
        break;
      case "L":
        x--;
        break;
      case "U":
        y++;
        break;
      case "D":
        y--;
        break;
    }
  }
  return x === 0 && y === 0;
};
```
