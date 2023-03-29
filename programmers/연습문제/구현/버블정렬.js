function solution1(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] > arr[j]) {
        const temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
      }
    }
  }
  return arr
}

function solution2(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[i]) {
        const temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
      }
    }
    console.log(arr)
  }
  return arr
}

// console.log(solution1([3, 2, 1]))
// console.log(solution2([3, 4, 2, 1]))
// console.log(solution1([3, 4, 5, 2, 6, 7, 9, 1, 8, 0]))
console.log(solution2([3, 4, 5, 2, 6, 7, 9, 1, 8, 0]))
