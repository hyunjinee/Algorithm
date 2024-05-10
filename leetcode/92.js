const reverseBetween = function (head, left, right) {
  const stack = []
  let leftNode = head
  let rightNode = head

  let count = 1

  while (left <= right) {
    if (count < left) {
      leftNode = leftNode.next
      rightNode = rightNode.next
      count++
      continue
    }

    if (count <= right) {
      stack.push(rightNode.val)
      rightNode = rightNode.next
      count++
      continue
    }

    leftNode.val = stack.pop()
    leftNode = leftNode.next
    left++
  }

  return head
}

// 스택에 넣었다가 고대로 빼면 ? => 뒤집어집니다요~
