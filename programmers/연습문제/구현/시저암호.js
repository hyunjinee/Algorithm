function solution(s, n) {
  return Array.from(s)
    .map((char) => {
      if (char === " ") return char

      const code = char.charCodeAt()

      const aCharCode = "a".charCodeAt()
      const zCharCode = "z".charCodeAt()
      const ACharCode = "A".charCodeAt()
      const ZCharCode = "Z".charCodeAt()

      if (aCharCode <= code && code <= zCharCode) {
        return String.fromCharCode(aCharCode + ((code - aCharCode + n) % 26))
      }

      if (ACharCode <= code && code <= ZCharCode) {
        return String.fromCharCode(ACharCode + ((code - ACharCode + n) % 26))
      }
    })
    .join("")
}

console.log(solution("AB", 1)) // "BC"
