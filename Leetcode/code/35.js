var searchInsert = function (nums, target) {
  let start = 0
  let end = nums.length - 1
  let mid = Math.floor((end - start) / 2)

  while (start <= end) {
    mid = Math.floor((start + end) / 2)
    if (nums[mid] == target) {
      return mid
    }
    if (nums[mid] > target) {
      end = mid - 1
    } else {
      start = mid + 1
    }
  }
  return start
}
