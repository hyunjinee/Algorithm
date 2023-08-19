const fs = require("fs")
const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
const [N, L] = inputs[0].split(" ").map(Number)
const numbers = inputs[1].split(" ").map(Number)

class Deque {
  constructor() {
    this.arr = []
    this.head = 0
    this.tail = 0
  }

  pushFront(value) {
    this.arr.unshift(value)
    this.tail++
  }

  popFront() {
    if (this.head < this.tail) {
      this.arr[this.head++]
    }
  }

  pushBack(value) {
    this.arr[this.tail++] = value
  }

  popBack() {
    if (this.head < this.tail) {
      this.arr[--this.tail]
    }
  }

  isEmpty() {
    return this.head >= this.tail
  }
}

let answer = ""
const deque = new Deque()

for (let i = 0; i < N; i++) {
  if (!deque.isEmpty() && deque.arr[deque.head][1] < i - L + 1) {
    deque.popFront()
  }
  const x = numbers[i]
  while (!deque.isEmpty() && deque.arr[deque.tail - 1][0] > x) {
    deque.popBack()
  }
  deque.pushBack([x, i])
  answer += deque.arr[deque.head][0] + " "
  if (i % 10000 === 0) {
    process.stdout.write(answer)
    answer = ""
  }
}

console.log(answer.trim())
