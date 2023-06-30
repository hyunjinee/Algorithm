const isBalanced = function (root) {
  if (root === null) return true

  let flag = true
  function helper(root) {
    if (root.left === null && root.right === null) {
      return 0
    }
    let leftHeight = 0,
      rightHeight = 0
    if (root.left !== null) {
      leftHeight = 1 + helper(root.left)
    }
    if (root.right !== null) {
      rightHeight = 1 + helper(root.right)
    }
    const actualHeight = Math.max(leftHeight, rightHeight)
    if (Math.abs(leftHeight - rightHeight) > 1) flag = false
    return actualHeight
  }
  helper(root)
  return flag
}
