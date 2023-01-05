var longestCommonPrefix = function (strs) {
  if (strs.length === 0) return "" // return for negative inputs
  if (strs.length === 1) return strs[0] // this case is not specified clearly in problem statement

  let finalStr = ""
  for (let i = 0; i < strs[0].length; i++) {
    // run loop on each character of first word
    let compareChar = strs[0][i] // f, fl, flo ..... and so on
    for (let j = 1; j < strs.length; j++) {
      let compareToChar = strs[j][i] // respective char of each word
      if (compareChar !== compareToChar) {
        return finalStr // If match is not found, it means we have longest prefix alredy, return it
      }
    }
    finalStr += compareChar // increase finalStr with another character
  }
  return finalStr
}
