const isSymmetric = function (root) {
  if (!root) return true
  return dfs(root.left, root.right)
}

function dfs(leftNode, rightNode) {
  if (!leftNode && !rightNode) {
    return true
  }
  if (
    (leftNode && !rightNode) ||
    (!leftNode && rightNode) ||
    leftNode.val !== rightNode.val
  ) {
    return false
  }
  return (
    dfs(leftNode.right, rightNode.left) && dfs(leftNode.left, rightNode.right)
  )
}
