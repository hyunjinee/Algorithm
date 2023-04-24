/**
 * @param {number[]} stones
 * @return {number}
 */
const lastStoneWeight = function (stones) {
  while (true) {
    sortStones()
    if (stones.length === 1) {
      return stones[0]
    }
    if (stones.length === 0) {
      return 0
    }

    let y = stones.shift()
    const x = stones.shift()

    if (y === x) {
      continue
    } else if (y > x) {
      y = y - x
      stones.push(y)
    }
  }

  function sortStones() {
    stones.sort((a, b) => b - a)
  }
}
