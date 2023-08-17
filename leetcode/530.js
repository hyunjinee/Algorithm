const getMinimumDifference = function (root) {
  const arr = []
  function inOrder(node) {
    if (node) {
      inOrder(node.left)
      arr.push(node.val)
      inOrder(node.right)
    }
  }
  inOrder(root)

  let minDiff = arr[1] - arr[0]
  for (let i = 2; i < arr.length; i++) {
    minDiff = Math.min(minDiff, arr[i] - arr[i - 1])
  }
  return minDiff
}
