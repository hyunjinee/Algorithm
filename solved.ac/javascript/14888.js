const stdin = require("fs").readFileSync("./dev/stdin").toString().trim()
const input = stdin.split("\n").map((v) => v.split(" ").map(Number))
const [N, A, operators] = input

const calculate = [(a, b) => a + b, (a, b) => a - b, (a, b) => a * b, (a, b) => parseInt(a / b)]

let max = -1_000_000_000
let min = 1_000_000_000

const dfs = (count = 0, result = A[0]) => {
  if (count === N - 1) {
    max = Math.max(max, result)
    min = Math.min(min, result)
  } else {
    for (let i = 0; i < 4; i++) {
      if (!operators[i]) {
        continue
      }
      operators[i]--
      dfs(count + 1, calculate[i](result, A[count + 1]))
      operators[i]++
    }
  }
}

dfs()
console.log(max)
console.log(min)

// const input = require("fs").readFileSync("./dev/stdin", "utf-8").toString().trim().split("\n")
// // const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
// console.log(input)

// const nums = input[1].spilt(" ").map(Number)
// const operators = input[2].split(" ").map(Number)
// let max = -Infinity,
//   min = Infinity

// const calculate = [(a, b) => a + b, (a, b) => a - b, (a, b) => a * b, (a, b) => parseInt(a / b)]

// const dfs = (count = 0  result = input[0]) => {
//   // if (count === )
// }
// // let max = -1_000_000_000;
// // let min = 1_000_000_000;

// // const dfs = (count = 0, result = A[0]) => {
// //   if (count === N - 1) {
// //     max = Math.max(max, result);
// //     min = Math.min(min, result);
// //   } else {
// //     for (let i = 0; i < 4 ; i++) {
// //       if (!operators[i]) {
// //         continue;
// //       }
// //       operators[i]--;
// //       dfs(count + 1, calculate[i](result, A[count + 1]));
// //       operators[i]++;
// //     }
// //   }
// // };

// // dfs();
// // console.log(max);
// // console.log(min);
// // function dfs(lv, idx) {}
// // const nums = input[1].split(" ").map((e) => +e)
// // const oa = input[2].split(" ").map((e) => +e)
// // let max = -Infinity,
// //   min = Infinity

// // dfs(nums[0], 0)
// // console.log(max + "\n" + min)

// // function dfs(lv, idx) {
// //   if (idx == input[0] - 1) {
// //     if (max < lv) max = lv
// //     if (min > lv) min = lv
// //   }
// //   for (let i = 0; i < 4; i++) {
// //     if (oa[i]) {
// //       oa[i]--
// //       dfs(calc(i, lv, nums[idx + 1]), idx + 1)
// //       oa[i]++
// //     }
// //   }
// // }

// // function calc(operator, l, r) {
// //   switch (operator) {
// //     case 0:
// //       return l + r
// //     case 1:
// //       return l - r
// //     case 2:
// //       return l * r
// //     case 3:
// //       return parseInt(l / r)
// //   }
// // }
