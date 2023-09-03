// class Node {
//   constructor(value) {
//     this.value = value
//     this.next = null
//     this.prev = null
//   }
// }

// class Deque {
//   constructor() {
//     this.head = null
//     this.tail = null
//     this.size = 0
//   }
//   pushFront(item) {
//     const newNode = new Node(item)
//     if (this.getSize() === 0) {
//       this.head = newNode
//       this.tail = newNode
//     } else {
//       newNode.next = this.head
//       this.head.prev = newNode
//       this.head = newNode
//     }
//     this.size += 1
//   }
//   pushBack(item) {
//     const newNode = new Node(item)
//     if (this.getSize() === 0) {
//       this.head = newNode
//       this.tail = newNode
//     } else {
//       this.tail.next = newNode
//       newNode.prev = this.tail
//       this.tail = newNode
//     }
//     this.size += 1
//   }
//   popFront() {
//     if (this.getSize() === 0) {
//       return -1
//     } else if (this.getSize() === 1) {
//       const popedItem = this.head.item
//       this.head = null
//       this.tail = null
//       this.size -= 1
//       return popedItem
//     } else if (this.getSize() === 2) {
//       const popedItem = this.head.item
//       this.head = this.head.next
//       this.tail.prev = null
//       this.size -= 1
//       return popedItem
//     } else if (this.getSize() > 2) {
//       const popedItem = this.head.item
//       this.head.next.prev = null
//       this.head = this.head.next
//       this.size -= 1
//       return popedItem
//     }
//   }
//   popBack() {
//     if (this.getSize() === 0) {
//       return -1
//     } else if (this.getSize() === 1) {
//       const popedItem = this.tail.item
//       this.head = null
//       this.tail = null
//       this.size -= 1
//       return popedItem
//     } else if (this.getSize() === 2) {
//       const popedItem = this.tail.item
//       this.tail = this.tail.prev
//       this.head.next = null
//       this.size -= 1
//       return popedItem
//     } else if (this.getSize() > 2) {
//       const popedItem = this.tail.item
//       this.tail.prev.next = null
//       this.tail = this.tail.prev
//       this.size -= 1
//       return popedItem
//     }
//   }
//   getSize() {
//     return this.size
//   }

//   isEmpty() {
//     return this.getSize() ? 0 : 1
//   }

//   getFront() {
//     return this.getSize() ? this.head.item : -1
//   }

//   getBack() {
//     return this.getSize() ? this.tail.item : -1
//   }
// }

// function solution(rc, operations) {
//   const left = new Deque()
//   const right = new Deque()
//   const mid = new Deque()

//   for (let i = 0; i < rc.length; i++) {
//     left.pushBack(rc[i][0])
//     right.pushBack(rc[i][rc[i].length - 1])

//     const temp = new Deque()

//     for (let j = 1; j < rc[0].length - 1; j++) {
//       temp.pushBack(rc[i][j])
//     }

//     mid.pushBack(temp)

//     console.log(mid.popBack())
//   }

//   for (const curr of operations) {
//     if (curr === "ShiftRow") {
//       left.pushFront(left.popBack())
//       right.pushFront(right.popBack())
//       mid.pushFront(mid.popBack())
//     } else {
//       // const top = mid.popFront()
//       // const bottom = mid.popBack()
//       // top.pushFront(left.popFront())
//       // bottom.pushBack(right.popBack())
//       // left.pushBack(bottom.popFront())
//       // right.pushFront(top.popBack())
//       // mid.pushFront(top)
//       // mid.pushBack(bottom)
//     }
//   }

//   const temp = mid.popFront()
//   console.log(mid, "what")
//   console.log(temp, "fucn?")

// console.log(left.popFront())
// console.log(temp.popFront())
// console.log(right.popFront())
// console.log(left.popFront())
// console.log(temp.popFront())
// console.log(right.popFront())
// console.log(left.popFront())
// console.log(temp.popFront())
// console.log(right.popFront())

// console.log(
//   Array(rc.length)
//     .fill()
//     .map((_, i) => {
//       const keep = mid.popFront()
//       console.log(keep)

//       console.log(JSON.stringify(keep, null, 2), "?")
//       const temp = []

//       console.log(left.popFront())
//       // console.log(keep.popBack())
//       console.log(right.popFront())
//       // while (keep.size > 0) {
//       // temp.push(keep.popFront())
//       // }
//       // return [left.popFront(), ...temp, right.popFront()]
//     })
// )
// }

class Node {
  constructor(item) {
    this.item = item
    this.next = null
    this.prev = null
  }
}
class Deque {
  constructor() {
    this.head = null
    this.tail = null
    this.size = 0
  }
  pushFront(item) {
    const newNode = new Node(item)
    if (this.getSize() === 0) {
      this.head = newNode
      this.tail = newNode
    } else {
      newNode.next = this.head
      this.head.prev = newNode
      this.head = newNode
    }
    this.size += 1
  }
  pushBack(item) {
    const newNode = new Node(item)
    if (this.getSize() === 0) {
      this.head = newNode
      this.tail = newNode
    } else {
      this.tail.next = newNode
      newNode.prev = this.tail
      this.tail = newNode
    }
    this.size += 1
  }
  popFront() {
    if (this.getSize() === 0) {
      return -1
    } else if (this.getSize() === 1) {
      const popedItem = this.head.item
      this.head = null
      this.tail = null
      this.size -= 1
      return popedItem
    } else if (this.getSize() === 2) {
      const popedItem = this.head.item
      this.head = this.head.next
      this.tail.prev = null
      this.size -= 1
      return popedItem
    } else if (this.getSize() > 2) {
      const popedItem = this.head.item
      this.head.next.prev = null
      this.head = this.head.next
      this.size -= 1
      return popedItem
    }
  }
  popBack() {
    if (this.getSize() === 0) {
      return -1
    } else if (this.getSize() === 1) {
      const popedItem = this.tail.item
      this.head = null
      this.tail = null
      this.size -= 1
      return popedItem
    } else if (this.getSize() === 2) {
      const popedItem = this.tail.item
      this.tail = this.tail.prev
      this.head.next = null
      this.size -= 1
      return popedItem
    } else if (this.getSize() > 2) {
      const popedItem = this.tail.item
      this.tail.prev.next = null
      this.tail = this.tail.prev
      this.size -= 1
      return popedItem
    }
  }
  getSize() {
    return this.size
  }

  isEmpty() {
    return this.getSize() ? 0 : 1
  }

  getFront() {
    return this.getSize() ? this.head.item : -1
  }

  getBack() {
    return this.getSize() ? this.tail.item : -1
  }
}

function solution(rc, operations) {
  const mdq = new Deque()
  const ldq = new Deque()
  const rdq = new Deque()
  let answer = [[]]
  for (let i = 0; i < rc.length; ++i) {
    const dq = new Deque()
    ldq.pushBack(rc[i][0])
    for (let j = 1; j < rc[0].length - 1; ++j) {
      dq.pushBack(rc[i][j])
    }
    rdq.pushBack(rc[i][rc[i].length - 1])
    mdq.pushBack(dq)

    // console.log(mdq.popBack())
  }
  for (let i = 0; i < operations.length; ++i) {
    if (operations[i] === "ShiftRow") {
      mdq.pushFront(mdq.popBack())
      ldq.pushFront(ldq.popBack())
      rdq.pushFront(rdq.popBack())
    } else if (operations[i] === "Rotate") {
      let sf = mdq.popFront()
      let sb = mdq.popBack()
      sf.pushFront(ldq.popFront())
      sb.pushBack(rdq.popBack())
      ldq.pushBack(sb.popFront())
      rdq.pushFront(sf.popBack())
      mdq.pushFront(sf)
      mdq.pushBack(sb)
    }
  }
  for (let i = 0; i < rc.length; ++i) {
    let arr = []
    let temp = mdq.popFront()
    temp.pushFront(ldq.popFront())
    temp.pushBack(rdq.popFront())
    for (let j = 0; j < rc[0].length; ++j) {
      arr[j] = temp.popFront()
    }
    answer[i] = arr
  }

  return answer
}

console.log(
  solution(
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ],
    ["Rotate", "ShiftRow"]
  )
)
