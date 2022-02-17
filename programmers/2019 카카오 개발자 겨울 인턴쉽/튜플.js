function solution(s) {
  let answer = []
  // console.log(s)
  let replaced = s
    .split("")
    .map((str) => str.replace("{", "[").replace("}", "]"))
  let arr = JSON.parse(replaced.join("")).sort((a, b) => a.length - b.length)
  // console.log(arr)

  arr.forEach((a) => answer.push(...a.filter((item) => !answer.includes(item))))
  return answer
}
