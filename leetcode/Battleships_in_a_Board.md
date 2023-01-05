# 419. Battleships in a Board

![419](https://user-images.githubusercontent.com/63354527/109620028-c5d27f80-7b7c-11eb-9f58-c042e4aa7012.PNG)

## 풀이 1

```javascript
var countBattleships = function (board) {
  let count = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (
        board[i][j] === "X" &&
        board[i][j - 1] !== "X" &&
        (!board[i - 1] || board[i - 1][j] !== "X")
      )
        count++;
    }
  }
  return count;
};
```

## 풀이 2

```javascript
const countBattleships = (board, result = 0) =>
  board.forEach((column, i) =>
    column.forEach((slot, j) =>
      slot === "X" &&
      (i === 0 || board[i - 1][j] === ".") &&
      (j === 0 || board[i][j - 1] === ".")
        ? (result += 1)
        : null
    )
  ) || result;
```
