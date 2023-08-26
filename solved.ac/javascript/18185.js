function buy1(n) {
  result += 3 * x[n]
}

function buy2(n) {
  let m = Math.min(x[n], x[n + 1])
  x[n] -= m
  x[n + 1] -= m
  result += 5 * m
}

function buy3(n) {
  let m = Math.min(x[n], x[n + 1], x[n + 2])
  x[n] -= m
  x[n + 1] -= m
  x[n + 2] -= m
  result += 7 * m
}

let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n")
let N = parseInt(input[0])
let x = input[1].split(" ").map(Number).concat([0, 0])
let result = 0

for (let i = 0; i < x.length - 2; i++) {
  if (x[i + 1] > x[i + 2]) {
    let m = Math.min(x[i], x[i + 1] - x[i + 2])
    x[i] -= m
    x[i + 1] -= m
    result += 5 * m
    buy3(i)
    buy1(i)
  } else {
    buy3(i)
    buy2(i)
    buy1(i)
  }
}

console.log(result)
// const fs = require("fs")
// const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

// // 라면 매니아 교준이네 집에는 N개의 라면 공장이 있음

// // 1번부터 N번까지의 공장이 있음

// // i번 공장에서 A[i]개의 라면을 살꺼임

// const n = +inputs.shift()
// const x = inputs.shift().split(" ").map(Number)

// let result = 0
// function buy1(n) {
//   result += 3 * x[n]
// }

// function buy2(n) {
//   let m = Math.min(x[n], x[n + 1])
//   x[n] -= m
//   x[n + 1] -= m
//   result += 5 * m
// }

// function buy3(n) {
//   let m = Math.min(x[n], x[n + 1], x[n + 2])
//   x[n] -= m
//   x[n + 1] -= m
//   x[n + 2] -= m
//   result += 7 * m
// }

// for (let i = 0; i < x.length - 2; i++) {
//   if (x[i + 1] > x[i + 2]) {
//     let m = Math.min(x[i], x[i + 1] - x[i + 2])
//     x[i] -= m
//     x[i + 1] -= m
//     result += 5 * m
//     buy3(i)
//     buy1(i)
//   } else {
//     buy3(i)
//     buy2(i)
//     buy1(i)
//   }
// }

// console.log(result)

// // for (let i = 0; i < n - 2; i++) {
// //   if (a[i + 1] > a[i + 2]) {
// //     const m = Math.min(a[i], a[i + 1] - a[i + 2])
// //     a[i] -= m
// //     a[i + 1] -= m
// //     ans += 5 * m
// //     buy3(i)
// //     buy1(i)
// //   } else {
// //     buy3(i)
// //     buy2(i)
// //     buy1(i)
// //   }
// // }
// // console.log(ans)
// // def buy1(n): # 1개 살 경우
// //     global result
// //     result += 3 * x[n]

// // def buy2(n): # 2개 살 경우
// //     global result
// //     m = min(x[n:n+2])
// //     x[n] -= m
// //     x[n+1] -= m
// //     result += 5* m

// // def buy3(n): # 3개 살 경우
// //     global result
// //     m = min(x[n:n+3])
// //     x[n] -= m
// //     x[n+1] -= m
// //     x[n+2] -= m
// //     result += 7* m

// // import sys
// // N = int(sys.stdin.readline())
// // x = list(map(int, sys.stdin.readline().split())) + [0,0]
// // result = 0
// // for i in range(len(x)-2):
// //     if x[i+1] > x[i+2]: # # 3번째가 더 작으면 -> [2, 3, 2, 1] 같은 케이스
// //         m = min(x[i], x[i+1] - x[i+2]) # x[i]랑 x[i+1]-x[i+2] 비교
// //         x[i] -= m
// //         x[i+1] -= m
// //         result += 5*m # 이 때는 3곳보단 2곳 사는게 이득
// //         buy3(i) # 남는 갯수는 3곳에서 사자
// //         buy1(i) # 마지막 남은건 그냥사자
// //     else :
// //         buy3(i)
// //         buy2(i)
// //         buy1(i)
// // print(result)
// // for (let i = 0; i < n - 2; i += 2) {
// //   while (a[i] > 0 && a[i + 1] > 0 && a[i + 2] > 0) {
// //     a[i]--
// //     a[i + 1]--
// //     a[i + 2]--
// //     ans += 7
// //   }
// // }

// // for (let i = 0; i < n - 1; i += 1) {
// //   while (a[i] > 0 && a[i + 1] > 0) {
// //     a[i]--
// //     a[i + 1]--
// //     ans += 5
// //   }
// // }

// // for (let i = 0; i < n; i += 1) {
// //   while (a[i] > 0) {
// //     a[i]--
// //     ans += 3
// //   }
// // }

// // console.log(ans)
