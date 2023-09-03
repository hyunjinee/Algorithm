function solution(numbers) {
  let temp = 1

  function inOrder(x) {
    const left = x.slice(0, Math.floor(x.length / 2))
    const mid = x[Math.floor(x.length / 2)]
    const right = x.slice(Math.floor(x.length / 2) + 1)

    console.log(left, mid, right, "/")
    if (mid === "0" && (left === "1" || right === "1")) {
      return false
    }

    if (mid === "1" && left === "0" && right === "0") {
      return true
    }

    if (mid === "0" && !left && !right) {
      return true
    }

    if (mid === "1" && !left && right) {
      return inOrder(right)
    }

    if (mid === "1" && left && !right) {
      return inOrder(left)
    }

    return inOrder(left) && inOrder(right)
  }

  const ans = []

  numbers.forEach((number) => {
    let bin = number.toString(2)
    const nodeCount = bin.length

    let depth = 1

    if (number === 1) {
    } else {
      while (true) {
        if (nodeCount ** depth - 1 > number) {
          break
        } else if (nodeCount ** depth - 1 == number) {
          break
        } else {
          depth += 1
        }
      }
    }

    while (bin.length !== 2 ** depth - 1) {
      bin = "0" + bin
    }

    ans.push(inOrder(bin))
  })

  // console.log(ans.map((x) => (x ? 1 : 0)))
  return ans.map((x) => (x ? 1 : 0))
}

solution([63, 111, 95]) // 1, 1, 0

// [true, true, false]

// [63, 111, 95]
