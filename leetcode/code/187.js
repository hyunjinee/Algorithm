const findRepeatedDnaSequences = function (s) {
  if (s.length < 10) return []
  let set = new Set(),
    res = new Set()
  let start = 0
  for (let end = 9; end < s.length; end++) {
    let substr = s.substring(start, end + 1)
    if (set.has(substr)) res.add(substr)
    else set.add(substr)
    start++
  }
  return Array.from(res)
}
