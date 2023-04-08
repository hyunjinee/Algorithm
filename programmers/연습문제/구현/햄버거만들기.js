function solution(ingredient) {
  let answer = 0
  ingredient = ingredient.join("")

  const ans = []

  for (let i = 0; i < ingredient.length; i++) {
    // console.log(ingredient[i])
    ans.push(ingredient[i])
    console.log(ans)
    const temp = ans.slice(-4)
    if (temp.length === 4 && temp.join("") === "1231") {
      ans.pop()
      ans.pop()
      ans.pop()
      ans.pop()
      answer++
    }
  }

  // while (true) {
  //   if (ingredient.includes("1231")) {
  //     ingredient = ingredient.replace("1231", "")
  //     answer++
  //   } else {
  //     break
  //   }
  // }

  // 이 풀이가 O(n ^ 2)이기 때문에 시간초과가 뜬다. 그리고 길이가 100만이기 때문에
  // O(n)으로 접근하려면 스택을 써야할듯
  return answer
}

console.log(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) // 2
