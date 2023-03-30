function solution(s) {
  return s
    .split(" ")
    .map((word) =>
      Array.from(word)
        .map((x, i) => {
          if (i % 2 == 0) {
            return x.toUpperCase()
          }

          return x.toLowerCase()
        })
        .join("")
    )
    .join(" ")
}
