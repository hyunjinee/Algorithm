function base10ToString(n) {
  let binaryString = ""

  function base10ToStringHelper(n) {
    console.log(n)
    if (n < 2) {
      binaryString += n
      return
    }

    base10ToStringHelper(Math.floor(n / 2))
    base10ToStringHelper(n % 2)
  }

  base10ToStringHelper(n)

  return binaryString
}

// console.log(base10ToString(232))
console.log(base10ToString(10))

// console.log(10 % 2)
