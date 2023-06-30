function mySqrt() {
  let left = 1,
    right = Math.floor(x / 2) + 1

  while (left <= right) {
    mid = Math.floor((left + right) / 2)

    if (mid * mid > x) {
      right = mid - 1
    } else if (mid * mid < x) {
      left = mid + 1
    } else {
      return mid
    }
  }

  return right
}
