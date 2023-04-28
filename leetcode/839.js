const numSimilarGroups = function (strs) {
  let result = 0

  if (!strs || strs.length === 0) {
    return 0
  }

  const visited = new Set()

  for (const str of strs) {
    if (!visited.has(str)) {
      dfs(str, strs, visited)
      result++
    }
  }

  function isSimilar(str1, str2) {
    let count = 0

    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) {
        count++

        if (count > 2) {
          return false
        }
      }
    }

    return count === 0 || count === 2
  }

  function dfs(str, strArr, visited) {
    if (visited.has(str)) {
      return
    }

    visited.add(str)

    for (let i = 0; i < strArr.length; i++) {
      if (isSimilar(str, strArr[i])) {
        dfs(strArr[i], strArr, visited)
      }
    }
  }

  return result
}
