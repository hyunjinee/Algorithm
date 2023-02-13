function sumOfLeftLeaves(root) {
  function traverse(node, isLeft) {
    if (node) {
      const { val, left, right } = node

      if (left || right) return traverse(left, true) + traverse(right, false)
      else return isLeft ? val : 0
    } else {
      return 0
    }
  }

  return traverse(root, false)
}
