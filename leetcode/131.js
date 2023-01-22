const partition = function (s) {
  const ans = []

  function backtracking(curr, index) {
    if (index >= s.length) {
      ans.push(curr)
      return
    }

    for (let i = index; i < s.length; i++) {
      if (isPalindrome(s.slice(index, i + 1))) {
        backtracking([...curr, s.slice(index, i + 1)], i + 1)
      }
    }
  }

  function isPalindrome(str) {
    return str === str.split("").reverse().join("")
  }

  backtracking([], 0)
  console.log(ans)
  return [...ans]
}

partition("cdd")
