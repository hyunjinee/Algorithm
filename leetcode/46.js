const permute = function (nums) {
  const res = []
  dfs(res, [], nums)
  return res
}

const dfs = (res, arr, nums) => {
  if (arr.length === nums.length) {
    res.push([...arr])
    return
  }
  for (let i = 0; i < nums.length; i++) {
    if (!arr.includes(nums[i])) dfs(res, [...arr, nums[i]], nums)
  }
}
