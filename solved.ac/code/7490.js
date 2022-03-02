const [N, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((i) => +i)

const solution = (N, arr) => {
  const getEquations = (n, count, sign, currentNum, sum, str) => {
    if (count === n) {
      const lastSum = sum + sign * currentNum
      if (lastSum === 0) {
        console.log(str)
      }
    } else {
      getEquations(
        n,
        count + 1,
        sign,
        currentNum * 10 + (count + 1),
        sum,
        `${str} ${count + 1}`
      )
      getEquations(
        n,
        count + 1,
        1,
        count + 1,
        sum + sign * currentNum,
        `${str}+${count + 1}`
      )
      getEquations(
        n,
        count + 1,
        -1,
        count + 1,
        sum + sign * currentNum,
        `${str}-${count + 1}`
      )
    }
  }
  for (let i = 0; i < N; i++) {
    getEquations(arr[i], 1, 1, 1, 0, "1")
    console.log()
  }
}

solution(N, arr)

// const [n, ...arr] = require("fs")
//   .readFileSync("./dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
//   .map((i) => +i)
// const solution = (n, arr) => {
//   console.log(n, arr)
//   const recursions = (n, count, sign, currentNum, sum, str) => {
//     if (count === n) {
//       const lastSum = sum + sign * currentNum
//       if (lastSum === 0) console.log(str)
//     } else {
//       recursions(
//         n,
//         count + 1,
//         sign,
//         currentNum * 10 + (count + 1),
//         sum,
//         `${str} ${count + 1}`
//       )
//       recursions(
//         n,
//         count + 1,
//         1,
//         count + 1,
//         sum + sign * currentNum,
//         `${str}+${count + 1}`
//       )
//       recursions(
//         n,
//         count + 1,
//         -1,
//         count + 1,
//         sum + sign * currentNum,
//         `${str}-${count + 1}`
//       )
//     }
//   }
//   for (let i = 0; i < n; i++) {
//     recursions(arr[i], 1, 1, 1, 0, "1")
//     console.log()
//   }
// }
// solution(n, arr)

// //       getEquations(
// //         n,
// //         count + 1,
// //         sign,
// //         currentNum * 10 + (count + 1),
// //         sum,
// //         `${str} ${count + 1}`
// //       )
// //       getEquations(
// //         n,
// //         count + 1,
// //         1,
// //         count + 1,
// //         sum + sign * currentNum,
// //         `${str}+${count + 1}`
// //       )
// //       getEquations(
// //         n,
// //         count + 1,
// //         -1,
// //         count + 1,
// //         sum + sign * currentNum,
// //         `${str}-${count + 1}`
// //       )
// //     }
// //   }
// //   for (let i = 0; i < N; i++) {
// //     getEquations(arr[i], 1, 1, 1, 0, "1")
// //     console.log()
// //   }
// // }

// // solution(N, arr)
