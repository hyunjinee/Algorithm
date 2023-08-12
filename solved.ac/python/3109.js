const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().split("\n")
const [r, c] = input[0].split(" ").map((e) => +e)
const board = input.slice(1)
const visited = Array.from({ length: r }, () =>
  Array.from({ length: c }, () => false)
)
let ans = 0
const dr = [-1, 0, 1]

function dfs(i, j) {
  if (j == c - 1) {
    return true
  }
  for (let d of dr) {
    if (
      0 <= i + d &&
      i + d < r &&
      board[i + d][j + 1] == "." &&
      !visited[i + d][j + 1]
    ) {
      visited[i + d][j + 1] = true
      if (dfs(i + d, j + 1)) {
        return true
      }
    }
  }
  return false
}
for (let i = 0; i < r; i++) {
  if (dfs(i, 0)) {
    ans += 1
  }
}
console.log(ans)
//i const [r, c, ...board] = input.split(" ")

// console.log(board)
// const board = Array.from(r + 1, () => new Array(c + 1))
// console.log(board)
// const board = Array.from((R + 1), () => new Array(C + 1));

// for(let i = 0; i < R; i++) {
//   board[i] = Array.from(input[i + 1]);
// }

// const dr = [-1, 0, 1];

// let canInstall = false;

// let answer = 0;

// for(let i = 0; i < R; i++) {
//   designPipeline(i, 0);
//   if (canInstall) answer += 1;
//   canInstall = false;
// }

// console.log(answer);

// function designPipeline (r, c) {
//   if (c === C - 1) {
//     canInstall = true;
//     return;
//   }

//   for(let k = 0; k < 3; k++) {
//     const nr = dr[k] + r;
//     const nc = 1 + c;

//     if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
//     if (board[nr][nc] == 'x' || board[nr][nc] == 'p') continue;

//     if (canInstall) return;

//     board[nr][nc] = 'p';
//     designPipeline(nr, nc);
//   }
// }

// function print () {
//   console.log(board.map((arr) => arr.join(' ')).join('\n'));
// }
