const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

/**
 * 쿠키런은 데브시스터즈에서 제작한 모바일 러닝 액션 게임이다.
 * 마녀의 오븐에서 탈출한 쿠키들과 함께 모험을 떠나는 게임으로,
 * 점프와 슬라이드 2가지 버튼만으로 손쉽게 플레이할 수 있는 것이 특징이다.
 * 연세대학교를 졸업한 김강산 선배님이 데브시스터즈에 취직하면서 주변 사람들에게 쿠키런을 전파시켰다.
 * 하지만 게임을 전파하던 중에 쿠키들에게 신체적으로 이상이 생기는 것을 발견하였다.
 * 팔, 다리 길이가 임의적으로 변한 것이다.
 * 때문에 긴급하게 각 쿠키들의 신체들을 측정하려고 한다.
 * 쿠키들은 신체를 측정하기 위해서 한 변의 길이가 N인 정사각형 판 위에 누워있으며, 어느 신체 부위도 판 밖으로 벗어나지 않는다.
 * 판의 x번째 행, y번째 열에 위치한 곳을 (x, y)로 지칭한다. 판의 맨 왼쪽 위 칸을 (1, 1), 오른쪽 아래 칸을 (N, N)으로 나타낼 수 있다.
 * 그림과 같이 쿠키의 신체는 머리, 심장, 허리, 그리고 좌우 팔, 다리로 구성되어 있다.
 * 그림에서 빨간 곳으로 칠해진 부분이 심장이다.
 * 머리는 심장 바로 윗 칸에 1칸 크기로 있다.
 * 왼쪽 팔은 심장 바로 왼쪽에 붙어있고 왼쪽으로 뻗어 있으며,
 * 오른쪽 팔은 심장 바로 오른쪽에 붙어있고 오른쪽으로 뻗어있다.
 * 허리는 심장의 바로 아래 쪽에 붙어있고 아래 쪽으로 뻗어 있다.
 * 왼쪽 다리는 허리의 왼쪽 아래에, 오른쪽 다리는 허리의 오른쪽 아래에 바로 붙어있고,
 * 각 다리들은 전부 아래쪽으로 뻗어 있다.
 * 각 신체 부위들은 절대로 끊겨있지 않으며 굽혀진 곳도 없다.
 * 또한, 허리, 팔, 다리의 길이는 1 이상이며, 너비는 무조건 1이다.
 */

// 변의 길이 N인 정사각형 판 위에 누워있음 쿠키
// 어느 신체 부위도 판 바깥에 없다.
// 맨 위 (1, 1), (N,N)

const n = +inputs.shift()
const board = inputs

let heart

function findHeart(board) {
  const n = board.length
  const m = board[0].length
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === "*") {
        heart = [i + 1, j]
        return
      }
    }
  }
  // for (let i = 0; i < n; i++) {
  //   const row = board[i]
  //   for (let j = 0; j < n; j++) {
  //     const col = row[j]
  //     if (col === "1") {
  //       heart = [i, j]
  //       break
  //     }
  //   }
  // }
}

findHeart(board)

// 하트를 찾았으면 이제 왼쪽 팔을 찾자.

let leftArm = 0

for (let i = 0; i < heart[1]; i++) {
  if (board[heart[0]][i] === "*") {
    leftArm += 1
  }
}

let rightArm = 0

for (let i = heart[1] + 1; i < board.length; i++) {
  if (board[heart[0]][i] === "*") {
    rightArm += 1
  }
}

let middle = 0

let lastPoint

for (let i = heart[0] + 1; i < board.length; i++) {
  if (board[i][heart[1]] === "*") {
    middle += 1
  } else {
    lastPoint = [i - 1, heart[1]]
    break
  }
}

// console.log(lastPoint, "last")
let leftLeg = 1
// for (let i = heart[0] + 1; i < board.length ;i++) {

// }

const isSafe = (x, y) => x >= 0 && x < board.length && y >= 0 && y < board.length
let i = 1
const leftStart = [lastPoint[0] + i, lastPoint[1] - i]
while (true) {
  const [cx, cy] = [leftStart[0] + i, leftStart[1]]
  if (!isSafe(cx, cy)) {
    break
  }

  if (board[cx][cy] === "*") {
    leftLeg += 1
  }
  i++
  // console.log("first")
}

let rightLeg = 1

let j = 1

const rightStart = [lastPoint[0] + j, lastPoint[1] + j]
while (true) {
  const [cx, cy] = [rightStart[0] + j, rightStart[1]]

  if (!isSafe(cx, cy)) {
    break
  }

  if (board[cx][cy] === "*") {
    rightLeg += 1
  }
  j++
}

console.log(heart[0] + 1, heart[1] + 1)
console.log(leftArm, rightArm, middle, leftLeg, rightLeg)
