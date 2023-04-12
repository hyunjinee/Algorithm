function solution(cards1, cards2, goal) {
  while (goal.length) {
    const next = goal.shift()

    if (cards1[0] === next) {
      cards1.splice(0, 1)
    } else if (cards2[0] === next) {
      cards2.splice(0, 1)
    } else {
      return "No"
    }
  }

  return "Yes"
}
