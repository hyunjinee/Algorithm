function solution(codeOwnersMap, directory) {
  const folders = directory.split("/")
  let i = 0

  function findOwner(structure, key) {
    const value = structure[key]
    // value에는 배열 또는 객체가 들어감. 근데 배열이라면 그대로 반환
    if (Array.isArray(value)) {
      return value
    }
    // value가 객체라면? i를 증가시켜서 다시 재귀호출
    i += 1
    return findOwner(value, folders[i])
  }
  return findOwner(codeOwnersMap, folders[i])
}
