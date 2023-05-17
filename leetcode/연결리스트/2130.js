const pairSum = function (head) {
  let result = []
  let arr = []
  let current = head

  while (current) {
    arr.push(current.val)
    current = current.next
  }

  arr.forEach((num, index) => {
    let sum = num + arr[arr.length - 1 - index]
    result.push(sum)
  })

  return Math.max(...result)
}
