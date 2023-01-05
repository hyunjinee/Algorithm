var searchInsert = function (nums, target) {
  if (nums.includes(target)) return nums.indexOf(target)
  for (let i = 0; i <= nums.length; i++) {
    if (target < nums[i]) return i
    else if (target > nums[i] && target < nums[i + 1]) return i + 1
  }
  return nums.length
}
