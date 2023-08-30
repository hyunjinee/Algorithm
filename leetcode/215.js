class MinHeap {
  constructor() {
    this.heap = []
  }

  size() {
    return this.heap.length
  }

  peek() {
    return this.heap[0]
  }

  add(value) {
    this.heap.push(value)
    this.bubbleUp(this.heap.length - 1)
  }

  poll() {
    const min = this.heap[0]
    const last = this.heap.pop()
    if (this.heap.length > 0) {
      this.heap[0] = last
      this.bubbleDown(0)
    }
    return min
  }

  bubbleUp(index) {
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2)
      if (this.heap[parentIndex] > this.heap[index]) {
        this.swap(parentIndex, index)
        index = parentIndex
      } else {
        break
      }
    }
  }

  bubbleDown(index) {
    while (index < this.heap.length) {
      let smallestChildIndex = index
      const leftChildIndex = index * 2 + 1
      const rightChildIndex = index * 2 + 2
      if (leftChildIndex < this.heap.length && this.heap[leftChildIndex] < this.heap[smallestChildIndex]) {
        smallestChildIndex = leftChildIndex
      }
      if (rightChildIndex < this.heap.length && this.heap[rightChildIndex] < this.heap[smallestChildIndex]) {
        smallestChildIndex = rightChildIndex
      }
      if (smallestChildIndex !== index) {
        this.swap(smallestChildIndex, index)
        index = smallestChildIndex
      } else {
        break
      }
    }
  }

  swap(i, j) {
    const temp = this.heap[i]
    this.heap[i] = this.heap[j]
    this.heap[j] = temp
  }
}
// class MinHeap {
//   constructor() {
//     this.heap = []
//   }

//   size() {
//     return this.heap.length
//   }

//   peek() {
//     return this.heap[0]
//   }

//   add(value) {
//     this.heap.push(value)
//     this.bubbleUp(this.heap.length - 1)
//   }

//   poll() {
//     const min = this.heap[0]
//     const last = this.heap.pop()

//     if (this.heap.length > 0) {
//       this.heap[0] = last
//       this.bubbleDown(0)
//     }

//     return min
//   }

//   bubbleUp(index) {
//     while (index > 0) {
//       const parentIndex = Math.floor((index - 1) / 2)

//       if (this.heap[parentIndex] > this.heap[index]) {
//         this.swap(parentIndex, index)
//         index = parentIndex
//       } else {
//         break
//       }
//     }
//   }

//   bubbleDown(index) {
//     while (index < this.heap.length) {
//       let smallestChildIndex = index
//       const leftChildIndex = 2 * index + 1
//       const rightChildIndex = 2 * index + 2

//       if (leftChildIndex < this.heap.length && this.heap[leftChildIndex] < this.heap[smallestChildIndex]) {
//         smallestChildIndex = leftChildIndex
//       }

//       if (rightChildIndex < this.heap.length && this.heap[rightChildIndex] < this.heap[smallestChildIndex]) {
//         smallestChildIndex = rightChildIndex
//       }

//       if (smallestChildIndex !== index) {
//         this.swap(smallestChildIndex, index)
//         index = smallestChildIndex
//       } else {
//         break
//       }
//     }
//   }

//   swap(i, j) {
//     const temp = this.heap[i]
//     this.heap[i] = this.heap[j]
//     this.heap[j] = temp
//   }
//   // constructor() {
//   //   this.heap = [null]
//   // }
//   // size() {
//   //   return this.heap.length - 1
//   // }
//   // getMin() {
//   //   return this.heap[1] ? this.heap[1] : null
//   // }
//   // swap(a, b) {
//   //   ;[this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]]
//   // }
//   // heappush(value) {
//   //   this.heap.push(value)
//   //   let curIdx = this.heap.length - 1
//   //   let parIdx = (curIdx / 2) >> 0
//   //   while (curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
//   //     this.swap(parIdx, curIdx)
//   //     curIdx = parIdx
//   //     parIdx = (curIdx / 2) >> 0
//   //   }
//   // }
//   // heappop() {
//   //   const min = this.heap[1]
//   //   if (this.heap.length <= 2) this.heap = [null]
//   //   else this.heap[1] = this.heap.pop()
//   //   let curIdx = 1
//   //   let leftIdx = curIdx * 2
//   //   let rightIdx = curIdx * 2 + 1
//   //   if (!this.heap[leftIdx]) return min
//   //   if (!this.heap[rightIdx]) {
//   //     if (this.heap[leftIdx] < this.heap[curIdx]) {
//   //       this.swap(leftIdx, curIdx)
//   //     }
//   //     return min
//   //   }
//   //   while (this.heap[leftIdx] < this.heap[curIdx] || this.heap[rightIdx] < this.heap[curIdx]) {
//   //     const minIdx = this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx
//   //     this.swap(minIdx, curIdx)
//   //     curIdx = minIdx
//   //     leftIdx = curIdx * 2
//   //     rightIdx = curIdx * 2 + 1
//   //   }
//   //   return min
//   // }
// }

const findKthLargest = function (nums, k) {
  const minHeap = new MinHeap()
  for (let num of nums) {
    minHeap.add(num)
    if (minHeap.size() > k) {
      minHeap.poll()
    }
  }
  console.log(minHeap.peek())
  return minHeap.peek()

  // without sorting.
  // nums.sort((a, b) => b - a)
  // console.log(nums)
  // return nums[k - 1]
}

findKthLargest([3, 2, 1, 5, 6, 4])
