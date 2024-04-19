// Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
// If target is not found in the array, return [-1, -1].
// You must write an algorithm with O(log n) runtime complexity.

// Time complexity: O(log n)
// 이분 탐색으로 접근가능해보인다.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const searchRange = function (nums, target) {
  let left = 0
  let right = nums.length - 1

  while (left <= right) {
    const mid = Math.floor((left + right) / 2)

    if (nums[mid] === target) {
      let start = mid
      let end = mid

      while (nums[start] === target) {
        start--
      }

      while (nums[end] === target) {
        end++
      }

      return [start + 1, end - 1]
    }

    if (nums[mid] < target) {
      left = mid + 1
    } else {
      right = mid - 1
    }
  }

  return [-1, -1]
}
