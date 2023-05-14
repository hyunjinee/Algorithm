const rotateString = function (s, goal) {
  if (s.length !== goal.length) return false
  return s.concat(s).includes(goal)
}
