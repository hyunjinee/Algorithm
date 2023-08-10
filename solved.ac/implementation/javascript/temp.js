const fs = require("fs")
const process = require("process")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
const dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
const [r, c] = input.shift().split(" ").map(Number)
const moves = input.pop()
let arduino = new Set()
let robot

for (let i = 0; i < r; i++) {
  for (let j = 0; j < c; j++) {
    if (input[i][j] === "I") {
      robot = [i, j]
    } else if (input[i][j] === "R") {
      arduino.add([i, j])
    }
  }
}

Array.from(moves).forEach((move, i) => {
  robot[0] += dx[move]
  robot[1] += dy[move]

  for (const [ax, ay] of arduino) {
    if (ax === robot[0] && ay === robot[1]) {
      console.log("kraj", i + 1)
      process.exit()
    }
  }

  const newArduino = new Set()
  const crushed = new Set()

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

    x += dx[m[0]]
    y += dy[m[0]]

    if (x === robot[0] && y === robot[1]) {
      console.log("kraj", i + 1)
      process.exit()
    }

    let flag = true
    for (const [ax, ay] of newArduino) {
      if (ax === x && ay === y) {
        crushed.add([x, y])
        flag = false
        break
      }
    }

    if (flag) {
      newArduino.add([x, y])
    }
  }

  for (const [x, y] of crushed) {
    Array.from(newArduino).forEach((v) => {
      if (v[0] === x && v[1] === y) {
        newArduino.delete(v)
      }
    })
  }

  arduino = newArduino
})

const board = Array.from(Array(r), () => Array(c).fill("."))
board[robot[0]][robot[1]] = "I"

for (const [x, y] of arduino) {
  board[x][y] = "R"
}

console.log(board.map((v) => v.join("")).join("\n"))
