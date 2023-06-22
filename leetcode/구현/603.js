const findTarget = function (root, k) {
  const set = new Set()
  return calc(root, k, set)
}

const calc = function (root, k, set) {
  if (root == null) {
    return false
  }
  if (set.has(k - root.val)) {
    return true
  }
  set.add(root.val)
  return calc(root.left, k, set) || calc(root.right, k, set)
}
