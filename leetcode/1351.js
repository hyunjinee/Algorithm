/**
 * @param {number[][]} grid
 * @return {number}
 */
const countNegatives = function (grid) {
  let result = 0

  grid.forEach((x) =>
    x.forEach((xx) => {
      if (xx < 0) {
        result++
      }
    })
  )

  return result
}
