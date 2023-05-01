function average(salary) {
  const max = Math.max(...salary)
  const min = Math.min(...salary)

  const sum = salary.reduce((a, x) => {
    if (x === max || x === min) return a
    return a + x
  }, 0)

  return sum / (salary.length - 2)
}
