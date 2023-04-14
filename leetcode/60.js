function permuteUnique(nums) {
  const ans = []
  const visited = Array(nums.length).fill(false)
  const set = new Set()
  backTracking([])

  function backTracking(arr) {
    if (arr.length === nums.length) {
      if (set.has(arr.join(""))) return

      set.add(arr.join(""))
      ans.push(arr)
      return
    }
    for (let i = 0; i < nums.length; i++) {
      if (!visited[i]) {
        arr.push(nums[i])
        visited[i] = true
        backTracking([...arr])
        arr.pop()
        visited[i] = false
      }
    }
  }
  return ans
}
