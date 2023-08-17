const canMakeArithmeticProgression = function (arr) {
  arr.sort((a, b) => a - b)
  let diff = Math.abs(arr[0] - arr[1])
  for (let i = 0; i < arr.length - 1; i++) {
    if (diff !== Math.abs(arr[i] - arr[i + 1])) {
      return false
    }
  }

  return true
}
