const maxArea = function (height) {
  const size = height.length
  let [left, right] = [0, size - 1]
  let maxWidth = size - 1
  let area = 0

  for (let width = maxWidth; width > 0; width--) {
    if (height[left] < height[right]) {
      area = Math.max(area, width * height[left])
      left += 1
    } else {
      area = Math.max(area, width * height[right])
      right -= 1
    }
  }
  return area
}
