const multiply = function (num1, num2) {
  if (num1 === "0" || num2 === "0") return "0"

  const n = num1.length,
    m = num2.length
  const ans = Array(m + n).fill(0)

  let currIdx = ans.length - 1

  for (let i = n - 1; i >= 0; i--) {
    let idx = currIdx--

    // console.log(idx)
    for (let j = m - 1; j >= 0; j--) {
      const res = +num1[i] * +num2[j] + ans[idx]
      ans[idx] = res % 10
      ans[--idx] += Math.floor(res / 10)

      // console.log(ans, idx)
    }

    // console.log(idx, "2")
  }
  return ans.join("").replace(/^0+/, "")
}

multiply("99", "99")
