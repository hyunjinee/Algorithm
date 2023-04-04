function checkTicTacToe(board, sign) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ]

  for (const [a, b, c] of lines) {
    if (board[a] == sign && board[b] == sign && board[c] == sign) return true
  }
  return false
}

function solution(board) {
  board = board.map((val) => val.split("")).flat()

  let [O, X] = [0, 0]

  for (const sign of board) {
    if (sign === "O") O++
    else if (sign === "X") X++
  }

  if (O < X || 1 < O - X) return 0

  let oWins = checkTicTacToe(board, "O")
  let xWins = checkTicTacToe(board, "X")

  if (oWins && xWins) return 0
  if (oWins && O - X !== 1) return 0
  if (xWins && O !== X) return 0

  return 1
}
