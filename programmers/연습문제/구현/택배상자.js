function solution(order) {
  const boxCount = order.length
  const boxes = Array.from({ length: boxCount }, (x, i) => i + 1)
  let ans = 0
  const stack = []

  while (order.length) {
    const want = order[0]
    const next = boxes[0]

    if (want === next) {
      order.shift()
      boxes.shift()
      ans++
      continue
    }

    if (want !== next) {
      if (stack[stack.length - 1] === want) {
        stack.pop()
        ans++
        order.shift()
        boxes.shift()
      }

      if (stack[stack.length] - 1 !== want) {
        stack.push(boxes.shift())
      }
    }

    if (order.length && stack.length === 0) {
      break
    }
  }
  console.log(ans)
  console.log(stack)
  return ans
}

solution([4, 3, 1, 2, 5], 2)
// solution([5, 4, 3, 2, 1], 5)
