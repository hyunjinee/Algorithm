const constructRectangle = function (area) {
  for (let n1 = Math.floor(Math.sqrt(area)); n1 >= 1; n1--) {
    let n2 = area / n1
    if (Number.isInteger(n2)) {
      let l = Math.max(n1, n2)
      let w = Math.min(n1, n2)
      return [l, w]
    }
  }
}
