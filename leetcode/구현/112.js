const isLeaf = (root) => !root.left && !root.right
const recursion = (root, targetSum) => {
  if (!root) return false
  if (isLeaf(root)) return targetSum - root.val === 0

  return recursion(root.left, targetSum - root.val) || recursion(root.right, targetSum - root.val)
}

const hasPathSum = (root, targetSum) => {
  return recursion(root, targetSum)
}
