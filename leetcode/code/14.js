var longestCommonPrefix = function (strs) {
  if (strs.length === 1) {
    return strs[0]
  }

  let returnStr = ""

  let counter = 0

  while (counter < strs[0].length) {
    let filterArr = strs.filter((word) => {
      return word[counter] === strs[0][counter]
    })
    if (filterArr.length !== strs.length) {
      return returnStr
    } else {
      returnStr += strs[0][counter]
      counter++
    }
  }
  return returnStr
}
