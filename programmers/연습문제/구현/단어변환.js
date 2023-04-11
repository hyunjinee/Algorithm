function solution(begin, target, words) {
  if (!words.includes(target)) {
    return 0
  }

  const q = [[begin, 0]]
  while (q.length) {
    const [currentWord, count] = q.shift()

    if (currentWord === target) {
      return count
    }

    const filtered = words.filter((x) => isOneCharDiff(currentWord, x))

    for (const f of filtered) {
      q.push([f, count + 1])
    }
  }

  return 0

  function isOneCharDiff(a, b) {
    let flag = false

    for (let i = 0; i < a.length; i++) {
      if (flag && a[i] !== b[i]) {
        return false
      }
      if (a[i] !== b[i]) {
        flag = true
      }
    }

    if (flag) {
      return true
    }

    return false
  }
}
