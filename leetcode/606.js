const tree2str = function (root) {
  const dfs = (node = root) => {
    if (!node) return ""

    const left = node.left ? "(" + dfs(node.left) + ")" : node.right ? "()" : ""
    const right = node.right ? "(" + dfs(node.right) + ")" : ""

    return node.val + left + right
  }

  return dfs()
}
