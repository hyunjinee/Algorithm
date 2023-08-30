const hasCycle = (head) => {
  while (head) {
    if (!head.val) return true

    head.val = null
    head = head.next
  }

  return false
}
