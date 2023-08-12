const fs = require("fs")
const lineReader = (dir) => {
  const file = fs.readFileSync(dir, "utf-8").split(/\r?\n/)
  let line = 0
  return () => file[line++]
}

const solution = () => {
  const input = lineReader("./dev/stdin")
  const n = Number(input())
  const k = Number(input())
  // console.log(n, k)
  const board = Array.from(Array(n + 1), () => new Array(n + 1).fill(0))
  // console.log(board)
  for (let i = 0; i < k; i++) {
    const [x, y] = input().split(" ").map(Number)
    board[x][y] = 2
  }
  const l = Number(input())
  const queue = []
  for (let i = 0; i < l; i++) {
    const [x, c] = input().split(" ")
    queue.push([Number(x), c])
  }
  console.log(move(board, queue, n))
}

const direction = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
] // N E S W

const move = (board, queue, n) => {
  const snake = [[1, 1]]
  let [x, y, dir] = [1, 1, 1]
  let time = 0
  board[1][1] = 1
  while (++time) {
    const [nx, ny] = [x + direction[dir][0], y + direction[dir][1]]
    if (nx <= 0 || ny <= 0 || nx > n || ny > n) break
    if (board[nx][ny] === 1) break
    snake.push([nx, ny])
    ;[x, y] = [nx, ny]
    if (board[nx][ny] !== 2) {
      const tail = snake.shift()
      board[tail[0]][tail[1]] = 0
    }
    board[nx][ny] = 1
    if (queue[0] && queue[0][0] === time) {
      const [t, nd] = queue.shift()
      dir = nd === "D" ? (dir + 1) % 4 : (dir - 1 + 4) % 4
    }
  }

  return time
}

solution()

//     // 이동 및 방향전환
//     if (queue[0] && queue[0][0] === time) {
//       const [t, nd] = queue.shift();
//       dir = nd === "D" ? (dir + 1) % 4 : (dir - 1 + 4) % 4;
//     }
//   }

//   return time;
// };

// solution();
