function solution(s) {
  if (isAllNumber(s)) {
    return Number(s)
  }

  const map = {
    zero: "0",
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  }

  for (const [key, value] of Object.entries(map)) {
    if (s.includes(key)) {
      s = s.replaceAll(key, value)
    }
  }

  return Number(s)
}

function isAllNumber(s) {
  return Array.from(s).every((e) => !isNaN(e))
}
