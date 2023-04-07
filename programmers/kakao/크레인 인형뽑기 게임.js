function solution(board, moves) {
  let answer = 0
  const baguni = []

  moves.forEach((move) => {
    move = move - 1
    if (isEmptyCol(move)) {
      return
    }
    for (let i = 0; i < board.length; i++) {
      if (board[i][move]) {
        if (baguni.length >= 1 && baguni[baguni.length - 1] == board[i][move]) {
          baguni.pop()
          answer += 2
          board[i][move] = 0
          break
        }

        baguni.push(board[i][move])
        board[i][move] = 0
        break
      }
    }
  })
  return answer

  function isEmptyCol(index) {
    let result = false
    if (board[board.length - 1][index] === 0) {
      result = true
    }

    return result
  }
}
