/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
function maxLevelSum(root) {
  if (root === null) {
    return -1 // or any appropriate value indicating an empty tree
  }

  let maxSum = -Infinity
  let maxLevel = -1

  // Perform level-order traversal using a queue
  const queue = [root]
  let level = 0

  while (queue.length > 0) {
    const levelSize = queue.length
    let currentLevelSum = 0

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift()
      currentLevelSum += node.val

      if (node.left !== null) {
        queue.push(node.left)
      }

      if (node.right !== null) {
        queue.push(node.right)
      }
    }

    if (currentLevelSum > maxSum) {
      maxSum = currentLevelSum
      maxLevel = level
    }

    level++
  }

  return maxLevel + 1
}
