const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const n = +inputs[0],
  arr = inputs.slice(1),
  start = arr.slice(0, n),
  end = arr.slice(n)
let result = 0
end.forEach((e) => {
  if (start[0] === e) {
    start.shift()
  } else {
    start.splice(start.indexOf(e), 1)
    result++
  }
})
console.log(result)

// for (let i = 0; i < n - 1; i++) {
//   for (let j = i + 1; j < n; j++) {
//     if (start[end[i]] > start[end[j]]) {
//       result++
//       break
//     }
//   }
// }

// console.log(result)
// start.forEach((s, startIndex) => {
//   const endIndex = end.indexOf(s)

//   if (endIndex < startIndex) {
//     result++
//   }
// })

// console.log(result)

// console.log(start, end)

// while (start.length && end.length) {
//   const s = start[0]
//   if (s === end[0]) {
//     start.shift()
//     end.shift()
//     continue
//   }

//   if (end[0] !== s) {
//     while (end.shift() === s) {
//       result += 1
//     }
//   }
// }

// console.log(result)

// const fs = require('fs');
// const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const N = +inputs[0];
// const before = {};
// inputs.slice(1, 1 + N).forEach((el, idx) => before[el] = idx);
// const after = inputs.slice(1 + N);

// let answer = 0;
// for (let i = 0 ; i < N - 1 ; i++) {
//     for (let j = i + 1 ; j < N ; j++) {
//         if (before[after[i]] > before[after[j]]) {
//             answer++;
//             break;
//         }
//     }
// }

// console.log(answer);
