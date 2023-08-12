const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [n, q] = inputs.shift().split(" ").map(Number)
const ducks = inputs.map(Number)
const visited = Array(n + 1).fill(0)
const ans = Array(q).fill(0)

ducks.forEach((duck, index) => {
  // 거슬러 올라감
  while (duck !== 1) {
    // 거슬러 올라가는 도중에 방문한적이 있다면
    if (visited[duck]) {
      // 정답에 넣어줌
      ans[index] = duck
    }
    duck = Math.floor(duck / 2)
  }
  // 방문한 적이 없다면 방문처리
  if (ans[index] === 0) {
    visited[ducks[index]] = true
  }
})
console.log(ans.join("\n"))

// const fs = require('fs');
// const [nums, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const [N, Q] = nums.split(' ').map(Number);
// const ducks = arr.map(Number);
// const answer = Array(Q).fill(0);
// const occupied = Array(N+1).fill(false);

// ducks.forEach((duck, idx, arr) => {

//     while (duck !== 1) {
//         if (occupied[duck]) {
//             answer[idx] = duck;
//         }
//         duck = Math.floor(duck / 2);
//     }

//     if (answer[idx] === 0) occupied[arr[idx]] = true;
// });

// console.log(answer.join('\n'));

// for (const num of arr) {
//   let result = 0
//   let t = num
//   while (t > 1) {
//     if (visited.includes(t)) {
//       result = t
//       break
//     }
//     t = Math.floor(t / 2)
//   }

//   if (!visited.includes(num)) {
//     visited.push(num)
//   }

//   console.log(result)
// }
// import sys
// n,q = map(int,input().split())
// num = []
// vis = set()
// for _ in range(q):
//     a = int(sys.stdin.readline().rstrip())
//     num.append(a)

// def visit(a):
//     ans = 0
//     b = a
//     while b > 0:
//         if b in vis:
//             ans = b
//         b//=2
//     if ans == 0:
//         vis.add(a)
//     print(ans)

// for i in num:
//     visit(i)
