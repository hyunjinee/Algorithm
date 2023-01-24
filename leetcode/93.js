const restoreIpAddresses = (s) => {
  if (s.length < 4 || s.length > 12) {
    return []
  }

  const ans = []

  const backtracking = (curr = [], index = 0) => {
    if (curr.length === 4) {
      ans.push(curr.join("."))
      return
    }

    if (curr.length === 3 && s.length - index > 3) {
      return
    }

    for (let i = 1; i <= 3; i++) {
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
