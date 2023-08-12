const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

class PriorityQueue {
  constructor() {
    this.heap = []
  }

  getLeftChildIndex(parentIndex) {
    if (parentIndex * 2 + 1 > this.heap.length - 1) return
    return parentIndex * 2 + 1
  }

  getRightChildIndex(parentIndex) {
    if (parentIndex * 2 + 2 > this.heap.length - 1) return
    return parentIndex * 2 + 2
  }
}

// const readline = require("readline")
// const rl = readline.createInterface({
//   input: process.stdin,
// constructor() {
//   this.queue = []
// }
// push(pos, oil) {
//   this.queue.push({ pos, oil })
//   this.up()
// }
// up() {
//   let i = this.queue.length - 1
//   const inserted = this.queue[i]
//   while (i > 0) {
//     const parent = Math.floor((i - 1) / 2)
//     if (this.queue[parent].oil < inserted.oil) {
//       this.queue[i] = this.queue[parent]
//       i = parent
//     } else break
//   }
//   this.queue[i] = inserted
// }
//   output: process.stdout,
// })
// let input = [],
//   n,
//   l,
//   p,
//   queue = [0],
//   result = 0,
//   isDone = false

// function enqueue(num) {
//   queue.push(num)
//   size = queue.length - 1
//   while (size > 1 && queue[Math.floor(size / 2)] < queue[size]) {
//     let temp = queue[Math.floor(size / 2)]
//     queue[Math.floor(size / 2)] = queue[size]
//     queue[size] = temp
//     size = Math.floor(size / 2)
//   }
// }
