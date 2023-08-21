const fs = require("fs")
const [n, ...inputs] = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const MIN = 301
const MAX = 1201

let answer = 0
const flowers = []

for (const input of inputs) {
  const flower = input.split(" ").map(Number)
  let start = flower[0] * 100 + flower[1]
  if (start < MIN) start = MIN

  let end = flower[2] * 100 + flower[3]
  if (end > MAX) end = MAX
  flowers.push([start, end])
}

const comp = (a, b) => {
  if (a[0] < b[0]) return -1
  else if (a[0] > b[0]) return 1
  else {
    if (a[1] < b[1]) return -1
    else return 1
  }
}

flowers.sort(comp)

let idx = 0
let end = MIN

while (flowers) {
  if (idx >= n || end >= MAX || flowers[idx][0] > end) break

  temp = -1
  for (let i = idx; i < n; i++) {
    if (flowers[i][0] <= end) {
      if (temp <= flowers[i][1]) {
        temp = flowers[i][1]
      }
      idx = i + 1
    } else {
      break
    }
  }
  end = temp
  answer += 1
}

console.log(end < MAX ? 0 : answer)

// // 3. 여러 줄의 값들을 입력받을 때
// const [N, ...input] = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n")

// // data = [피는월,피는날,지는월,지는날]
// /*
// 첫번쨰 : 3월 2일 이전에 피는 꽃 중에 지는 시기가 가장 늦는 꽃
// 이게 없으면 0 출력

// 이후 선택 : 직전 꽃이 지는 시기 이전에 피는 꽃 중에 지는 시기가 가장 늦는 꽃

// 그게 없으면 0 출력
// 정렬은 지는 시기의 내림차순
// */
// let count = 0
// let currFlower
// let visited = Array(Number(N)).fill(false)
// let board = input.map((e) => {
//   return e.split(" ").map(Number)
// })

// board.sort((a, b) => {
//   if (b[2] != a[2]) {
//     return b[2] - a[2]
//   }
//   return b[3] - a[3]
// })

// //첫 출발 꽃 뽑기

// for (let i = 0; i < board.length; i++) {
//   if (board[i][0] >= 4) continue // 4월 이상 리턴
//   if (board[i][0] == 3 && board[i][1] >= 2) continue // 3월 중 2일 이상 리턴
//   currFlower = [...board[i]]
//   visited[i] = true
//   count++
//   break
// }

// if (!currFlower) {
//   console.log(0)
//   return
// }
// let x = currFlower[0] * 100 + currFlower[1]
// let y = currFlower[2] * 100 + currFlower[3]
// if (x <= 301 && y >= 1201) {
//   console.log(1)
//   return
// }

// if (board.length == 1) {
//   if (currFlower[2] <= 11 && currFlower[3] <= 31) console.log(0)
//   else console.log(1)
//   return
// }

// //이후 선택 : 직전 꽃이 지는 시기 이전에 피는 꽃 중에 지는 시기가 가장 늦는 꽃
// let i = 0
// while (i < board.length) {
//   if (visited[i] == true) {
//     i++
//     continue
//   }
//   if ((board[i][0] == currFlower[2] && board[i][1] <= currFlower[3]) || board[i][0] < currFlower[2]) {
//     count++
//     currFlower = [...board[i]]
//     if (currFlower[2] === 12) break
//     visited[i] = true
//     i = -1
//   }
//   i++
// }

// i == board.length ? console.log(0) : console.log(count)
