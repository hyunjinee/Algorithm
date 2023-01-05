var findMedianSortedArrays = function (nums1, nums2) {
  const mergedArray = [...nums1, ...nums2].sort((a, b) => a - b)
  let median

  // if length of merged array is even then get the mid two numbers and find median
  if (mergedArray.length % 2 === 0) {
    median =
      (mergedArray[mergedArray.length / 2 - 1] +
        mergedArray[mergedArray.length / 2]) /
      2
  } else {
    // if length is odd then mid number is median
    median = mergedArray[Math.floor(mergedArray.length / 2)]
  }

  return median
}
