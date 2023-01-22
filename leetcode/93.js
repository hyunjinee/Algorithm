const restoreIpAddresses = (s) => {
  if (s.length < 4 || s.length > 12) {
    return [] // 4 보다 길이가 작으면 빈 배열 반환
  }

  const ans = [] // 정답 배열 선언
  const backtracking = (curr = [], index = 0) => {
    if (curr.length === 4) {
      ans.push(curr.join(".")) // 베이스 케이스 4개 다차면 ans에 추가
      return
    }

    if (curr.length === 3 && s.length - index > 3) {
      return
    }

    for (let i = 1; i <= 3; i++) {
      // 0으로 시작하는 숫자는 제외
      if (s[index] === "0") {
        backtracking([...curr, "0"], index + 1)
        break
      }

      if (Number(s[index]) >= 1 && Number(s[index]) <= 9) {
        if (Number(s.slice(index, index + i)) > 255) {
          break
        }

        curr.push(s.slice(index, index + i))
        backtracking(curr, index + i)
        curr.pop()
      }
    }
  }

  backtracking()
  return [...new Set(ans.filter((e) => e.length === s.length + 3))]
}

restoreIpAddresses("25525511135")
