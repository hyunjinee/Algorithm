const searchInsert = function (nums, target) {
  if (nums.includes(target)) return nums.indexOf(target)
  for (let i = 0; i <= nums.length; i++) {
    if (target < nums[i]) return i
    else if (target > nums[i] && target < nums[i + 1]) return i + 1
  }
  return nums.length
}

// var searchInsert = function (nums, target) {
//   let start = 0
//   let end = nums.length - 1
//   let mid = Math.floor((end - start) / 2)

//   while (start <= end) {
//     mid = Math.floor((start + end) / 2)
//     if (nums[mid] == target) {
//       return mid
//     }
//     if (nums[mid] > target) {
//       end = mid - 1
//     } else {
//       start = mid + 1
//     }
//   }
//   return start
// }
