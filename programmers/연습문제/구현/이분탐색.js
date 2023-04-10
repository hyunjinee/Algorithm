function binarySearch(arr, target) {
  let start = 0
  let end = arr.length - 1
  let mid = Math.floor((start + end) / 2)

  while (start <= end) {
    mid = Math.floor((start + end) / 2)
    if (arr[mid] === target) {
      return mid
    } else if (arr[mid] > target) {
      end = mid - 1
    } else {
      start = mid + 1
    }
  }
}

console.log(binarySearch([1, 3, 5, 7, 9], 3)) // 1
