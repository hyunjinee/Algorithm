/**
 * @param {Node} head
 * @return {Node}
 */
const copyRandomList = function (head) {
  if (!head) return null

  const oldToNew = new Map()

  let curr = head
  while (curr) {
    oldToNew.set(curr, new Node(curr.val))
    curr = curr.next
  }

  curr = head
  while (curr) {
    oldToNew.get(curr).next = oldToNew.get(curr.next) || null
    oldToNew.get(curr).random = oldToNew.get(curr.random) || null
    curr = curr.next
  }

  return oldToNew.get(head)
}
