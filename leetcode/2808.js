/**
 * @param {number[]} nums
 * @return {number}
 */
const minimumSeconds = function (nums) {}

//

// /**
//  * @param {number[]} nums
//  * @return {number}
//  */
// var minimumSeconds = function(nums) {
//   // find max distance to number that is not the same
//   const hashMap = new Map()
//   for (let i = 0; i < nums.length; i++) {
//       let num = nums[i]
//       if (hashMap.has(num)) {
//           let indexes = hashMap.get(num)
//           indexes.push(i)
//           hashMap.set(num, indexes)
//       } else {
//           hashMap.set(num, [i])
//       }
//   }
//   let answer = Infinity
//   hashMap.forEach((indexes, num) => {
//       let maxDistForNum = -1 * Infinity
//       let firstIndex = indexes[0]
//       let lastIndex = indexes[indexes.length - 1]
//       maxDistForNum = Math.max(maxDistForNum, nums.length - lastIndex + firstIndex)

//       for (let i = 1 ; i< indexes.length; i++) {
//           let prevIndex = indexes[i - 1]
//           let curIndex = indexes[i]
//           maxDistForNum = Math.max(maxDistForNum, curIndex - prevIndex)
//       }
//       answer = Math.min(answer, maxDistForNum)
//   })
//   return Math.floor(answer / 2)
// };
