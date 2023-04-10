function solution(m, n, board) {
  let ans = 0
  board = board.map((b) => Array.from(b))
  while (true) {
    const q = []
    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        const set = new Set()

        for (let k = 0; k < 2; k++) {
          for (let l = 0; l < 2; l++) {
            set.add(board[i + k][j + l])
          }
        }

        if (set.size === 1) {
          for (let k = 0; k < 2; k++) {
            for (let l = 0; l < 2; l++) {
              if (board[i + k][j + l] == ".") {
                continue
              }
              q.push([i + k, j + l])
            }
          }
        }
      }
    }

    if (q.length === 0) {
      break
    }

    while (q.length) {
      const [y, x] = q.shift()
      if (board[y][x] != ".") {
        board[y][x] = "."
        ans++
      }
    }

    for (let i = m - 1; i > 0; i--) {
      for (let j = 0; j < n; j++) {
        if (board[i][j] == ".") {
          for (let k = i - 1; k >= 0; k--) {
            if (board[k][j] !== ".") {
              board[i][j] = board[k][j]
              board[k][j] = "."
              break
            }
          }
        }
      }
    }
  }

  return ans
}
