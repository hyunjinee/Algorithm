function flatten(arr) {
  return (function f(arr, newArr) {
    arr.forEach((v) => (Array.isArray(v) ? f(v, newArr) : newArr.push(v)))
    return newArr
  })(arr, [])
}
console.log(
  flatten([
    [1, 2],
    [3, 4],
    [5, 6, 7],
  ])
)
