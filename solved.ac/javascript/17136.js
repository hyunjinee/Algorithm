const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const board = inputs.map((line) => line.split(" ").map(Number))
const visited = Array(10).fill(Array(10).fill(false))

let ans = Infinity
const paper = [0, 5, 5, 5, 5, 5]
function updateBoard(x, y, size, state) {
  for (let i = x; i < x + size; i++) {
    for (let j = y; j < y + size; j++) {
      board[i][j] = state
    }
  }
}

function canAttachPaper(x, y, size) {
  // x+size, y+size가 범위 안에 들어오고, 모두 1일 때
  if (x + size > 10 || y + size > 10) return false
  for (let i = x; i < x + size; i++) {
    for (let j = y; j < y + size; j++) {
      if (board[i][j] == 0) return false
    }
  }
  return true
}

function dfs(x, y, cnt) {
  if (x >= 9 && y > 9) {
    // x나 y가 범위의 끝에 도달했을 때
    ans = Math.min(ans, cnt)
    return
  }
  if (ans <= cnt) return // 현재 cnt가 최솟값이 될 수 없을 때

  if (y > 9) {
    // 다음 줄 탐색
    dfs(x + 1, 0, cnt)
    return
  }

  if (board[x][y] == 1) {
    for (let size = 5; size > 0; size--) {
      if (paper[size] > 0 && canAttachPaper(x, y, size)) {
        // 길이가 size인 종이가 남아있고, x+size, y+size가 범위 안에 들어오고, 모두 1일 때
        updateBoard(x, y, size, 0) // size만큼을 0으로 (색종이 붙이기)
        paper[size]--
        dfs(x, y + 1, cnt + 1)
        updateBoard(x, y, size, 1) // size만큼을 다시 1로 (색종이 떼기)
        paper[size]++
      }
    }
  } else {
    dfs(x, y + 1, cnt)
  }
}
dfs(0, 0, 0)
if (ans == Infinity) console.log(-1)
else console.log(ans)
