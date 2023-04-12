const putComma = (s) => {
  if (s.length <= 3) return s
  return putComma(s.slice(0, -3)) + "," + s.slice(-3)
}

console.log(putComma("123456789"))
