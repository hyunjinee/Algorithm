function binarySearch(array, target) {
  let [start, end] = [0, array.length - 1]

  while (start <= end) {
    let mid = Math.floor((start + end) / 2)

    if (array[mid] === target) {
      return mid
    }

    if (target < array[mid]) {
      end = mid - 1
    } else {
      start = mid + 1
    }
  }
  return -1
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)) // 4
// console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
