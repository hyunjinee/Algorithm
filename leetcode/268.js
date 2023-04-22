/**
 * @param {number[]} nums
 * @return {number}
 */
const missingNumber = function (nums) {
  const n = nums.length // n은 nums의 길이
  const diff = Array(n + 1)
    .fill()
    .map((x, i) => i) // 0부터 n까지의 배열을 만든다.

  nums.sort() // nums를 정렬한다.

  for (let i = 0; i < n; i++) {
    diff.splice(diff.indexOf(nums[i]), 1) // diff에 있는 nums[i] 삭제
  }

  return diff[0] // 나머지 하나가 빠진 숫자이다.
}
