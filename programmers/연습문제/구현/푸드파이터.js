function solution(food) {
  food = food.map((f, i) => {
    if (i == 0) return f
    if (f % 2 === 1) {
      return f - 1
    }

    return f
  })

  food = food.slice(1)

  let s = ""

  food = food.map((x) => x / 2)

  for (let i = 0; i < food.length; i++) {
    const count = food[i]

    for (let j = 0; j < count; j++) {
      s += String(i + 1)
    }
  }

  const reversed = s.split("").reverse().join("")

  return s + "0" + reversed
}
