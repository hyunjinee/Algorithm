function calcul(gen, num) {
  if (gen == 1) return "Rr"
  if (gen == 2) {
    if (num == 1) return "RR"
    else if (num == 2 || num == 3) return "Rr"
    else return "rr"
  }
  let parent = calcul(gen - 1, Math.ceil(num / 4))
  if (parent == "rr") return "rr"
  if (parent == "RR") return "RR"
  if (parent == "Rr") {
    return calcul(2, num % 4)
  }
}
function solution(queries) {
  return queries.map((query) => calcul(query[0], query[1]))
}
