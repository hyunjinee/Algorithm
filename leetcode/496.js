/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
const nextGreaterElement = function (nums1, nums2) {
  const temp = []
  for (const num of nums1) {
    if (nums2.indexOf(num) === nums2.length - 1) {
      temp.push(-1)
      continue
    }
    const sliced = nums2.slice(nums2.indexOf(num))
    const index = sliced.findIndex((x) => x > num)
    if (index === -1) {
      temp.push(-1)
      continue
    }
    temp.push(sliced[index])
  }

  return temp
}
