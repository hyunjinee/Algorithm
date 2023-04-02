function solution(citations) {
  citations.sort((a, b) => b - a)

  console.log(citations)
  for (let i = 0; i < citations.length; i++) {
    if (i >= citations[i]) {
      return i
    }
  }
  return citations.length
}
