const intersect = function (nums1, nums2) {
  const result = []

  for (const n of nums1) {
    const index = nums2.indexOf(n)

    if (index === -1) {
      continue
    }
    result.push(n)
    nums2.splice(index, 1)
  }

  return result
}
