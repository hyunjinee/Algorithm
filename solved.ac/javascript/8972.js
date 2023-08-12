const fs = require("fs")
const process = require("process")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
const dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
const [r, c] = input.shift().split(" ").map(Number)
const moves = input.pop()
let arduino = []
let robot

for (let i = 0; i < r; i++) {
  for (let j = 0; j < c; j++) {
    if (input[i][j] === "I") {
      robot = [i, j]
    } else if (input[i][j] === "R") {
      arduino.push([i, j])
    }
  }
}
console.log(arduino)

Array.from(moves).forEach((move, i) => {
  // 내 로봇 이동
  robot[0] += dx[move]
  robot[1] += dy[move]

  // 내 로봇이 이동한 위치가 아두이노면 사망
  for (const [ax, ay] of arduino) {
    if (ax == robot[0] && ay == robot[1]) {
      console.log("kraj", i + 1)
      process.exit()
    }
  }

  let newArduino = []
  let crushed = []

  for (let [x, y] of arduino) {
    let m = [5, 201]

    for (let j = 1; j < 10; j++) {
      const ax = x + dx[j]
      const ay = y + dy[j]
      const distance = Math.abs(ax - robot[0]) + Math.abs(ay - robot[1])

      if (distance < m[1]) {
        m = [j, distance]
      }
    }

    // 아두이노를 가장 가깝게 이동
    x += dx[m[0]]
    y += dy[m[0]]

    // 내 로봇이랑 충돌시 사망
    if (x === robot[0] && y === robot[1]) {
      console.log("kraj", i + 1)
      process.exit()
    }

    newArduino.push([x, y])

    // 내 로봇이랑 충돌하지 않았으면 다른 아두이노랑 충돌하지 않았는지 체크

    for (let [ax, ay] of arduino) {
      // 다른 아두이노랑 충돌했으면?
      if (ax === x && ay === y) {
        crushed.push([x, y])
        flag = false
        break
      }
    }

    newArduino = newArduino.filter(([x, y]) => {
      for (let [ax, ay] of crushed) {
        if (ax === x && ay === y) {
          return false
        }
      }
    })
  }

  // 새로운 아두이노 위치로 갱신
  arduino = newArduino
})

const board = Array.from(Array(r), () => Array(c).fill("."))
board[robot[0]][robot[1]] = "I"

for (const [x, y] of arduino) {
  board[x][y] = "R"
}

console.log(board.map((v) => v.join("")).join("\n"))

//   // 충돌좌표
//   const crushed = []

//   for (let [x, y] of arduino) {
//     let m = [5, 201]

//     for (let j = 1; j < 10; j++) {
//       const ax = x + dx[j]
//       const ay = y + dy[j]
//       const distance = Math.abs(ax - robot[0]) + Math.abs(ay - robot[1])

//       if (distance < m[1]) {
//         m = [j, distance]
//       }
//     }

//     // 아두이노를 가장 가깝게 이동
//     x += dx[m[0]]
//     y += dy[m[0]]

//     // 내 로봇이랑 충돌시 사망
//     if (x === robot[0] && y === robot[1]) {
//       console.log("kraj", i + 1)
//       process.exit()
//     }

//     for (const [ax, ay] of newArduino) {
//       if (ax === x && ay === y) {
//         crushed.push([x, y])
//         break
//       }
//     }

//     newArduino.push([x, y])
//   }

//   for (const [x, y] of crushed) {
//     newArduino = newArduino.filter((v) => v[0] != x && v[1] != y)
//   }

//   arduino = newArduino
// })

// const board = Array.from(Array(r), () => Array(c).fill("."))
// board[robot[0]][robot[1]] = "I"

// for (const [x, y] of arduino) {
//   board[x][y] = "R"
// }

// console.log(board.map((v) => v.join("")).join("\n"))
