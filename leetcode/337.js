const rob = function (root) {
  const dfs = (root) => {
    if (!root) return [0, 0]

    const left = dfs(root.left)
    const right = dfs(root.right)

    const withRoot = root.val + left[1] + right[1]
    const withoutRoot = Math.max(...left) + Math.max(...right)

    return [withRoot, withoutRoot]
  }

  return Math.max(...dfs(root))
}
