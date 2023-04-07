function solution(userId, bannedId) {
  const bannedSet = new Set()
  const visited = Array(userId.length).fill(0)

  backTracking(0)

  function backTracking(depth) {
    if (bannedId.length === depth) {
      bannedSet.add(visited.join(""))
      return
    }

    for (let i = 0; i < userId.length; i++) {
      if (!visited[i] && isSame(userId[i], bannedId[depth])) {
        visited[i] = 1
        backTracking(depth + 1)
        visited[i] = 0
      }
    }
  }

  function isSame(userId, bannedId) {
    if (userId.length !== bannedId.length) {
      return false
    }
    for (let i = 0; i < bannedId.length; i++) {
      if (bannedId[i] === "*") {
        continue
      } else if (userId[i] !== bannedId[i]) {
        return false
      }
    }

    return true
  }

  return bannedSet.size
}
