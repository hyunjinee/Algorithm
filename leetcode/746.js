const minCostClimbingStairs = function (cost) {
  let even = cost[0]
  let odd = cost[1]

  for (let i = 2; i < cost.length; i++) {
    if (i % 2) {
      odd = Math.min(odd + cost[i], even + cost[i])
    } else {
      even = Math.min(even + cost[i], odd + cost[i])
    }
  }

  return Math.min(odd, even)
}
