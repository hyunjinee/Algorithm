/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
const leafSimilar = function (root1, root2) {
  // dfs 방식으로 leaf search

  const leaf1 = [],
    leaf2 = []

  dfs(root1, leaf1)
  dfs(root2, leaf2)

  function dfs(root, arr) {
    if (!root.val) {
      return
    }

    if (!root.left && !root.right) {
      arr.push(root.val)
      return
    }

    if (root.left) {
      dfs(root.left, arr)
    }

    if (root.right) {
      dfs(root.right, arr)
    }
  }

  return leaf1.length === leaf2.length && leaf1.every((leaf, i) => leaf === leaf2[i])
}
