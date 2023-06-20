/**
 * @param {number[]} score
 * @return {string[]}
 */
const findRelativeRanks = function (score) {
  const newScore = score.sort((a, b) => b - a)
  const mapRes = new Map()

  for (let i = 0; i < newScore.length; i++) {
    mapRes.set(newScore[i], i)
  }
  // rewrite each value with there places
  for (let i = 0; i < score.length; i++) {
    score[i] = "" + (mapRes.get(score[i]) + 1)
    if (score[i] === "1") score[i] = "Gold Medal"
    if (score[i] === "2") score[i] = "Silver Medal"
    if (score[i] === "3") score[i] = "Bronze Medal"
  }
  return score
}
