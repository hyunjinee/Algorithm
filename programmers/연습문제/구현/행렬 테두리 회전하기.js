function solution(rows, columns, queries) {
  const answer = []
  let arr = Array.from(new Array(rows + 1), () =>
    new Array(columns + 1).fill(0)
  )

  // 숫자 채우기
  for (let i = 1; i <= rows; i++) {
    for (let j = 1; j <= columns; j++) {
      arr[i][j] = (i - 1) * columns + j
    }
  }

  for (let tc = 0; tc < queries.length; tc++) {
    const [x1, y1, x2, y2] = queries[tc]
    const stack = []
    // 맨 위 직사각형 고르기 x1은 행 고정, y1이 y2 직전까지 1씩 증가
    for (let i = y1; i < y2; i++) stack.push(arr[x1][i])
    // 오른쪽 직사각형 고르기 y2는 고정, x1이 x2 직전까지 1씩 증가
    for (let i = x1; i < x2; i++) stack.push(arr[i][y2])
    // 아래쪽 직사각형 고르기 x2는 고정, y2가 y1 직전까지 1씩 감소
    for (let i = y2; i > y1; i--) stack.push(arr[x2][i])
    // 왼쪽 직사각형 고르기y1는 고정, x2가 x1 직전까지 1씩 감소
    for (let i = x2; i > x1; i--) stack.push(arr[i][y1])
    // 정답 찾기
    answer.push(Math.min(...stack))
    const temp = stack.pop()
    stack.unshift(temp)

    for (let i = y1; i < y2; i++) arr[x1][i] = stack.shift()
    for (let i = x1; i < x2; i++) arr[i][y2] = stack.shift()
    for (let i = y2; i > y1; i--) arr[x2][i] = stack.shift()
    for (let i = x2; i > x1; i--) arr[i][y1] = stack.shift()
  }

  return answer
}
