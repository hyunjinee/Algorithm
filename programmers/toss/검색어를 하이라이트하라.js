const exclude = ","

function solution(text, keyword) {
  if (keyword.length === 0) return text
  const ans = []
  const textArr = Array.from(text)
  const comma = []
  const commaIndex = []

  textArr.forEach((char, index) => {
    if (char === exclude) {
      comma.push(index)
    }
  })

  for (let i = 0; i <= text.length - keyword.length; i = i + 1) {
    const temp = text.slice(i, i + keyword.length)
    console.log(temp)

    let commaCount = 0

    for (let j = 0; j < temp.length; j = j + 1) {
      if (temp[j] === exclude) {
        commaCount += 1
      }
    }

    console.log(commaCount)
    const real = text.slice(i, i + keyword.length + commaCount)
    let realWithOutComma

    if (real.startsWith(",")) {
      continue
    } else {
      realWithOutComma = real.replace(/,/g, "")
    }
    if (realWithOutComma === keyword) {
      ans.push([i, i + keyword.length + commaCount])
    }
  }

  console.log(ans)

  ans.forEach(([start, end]) => {
    textArr.splice(end, 0, "</mark>")
    textArr.splice(start, 0, "<mark>")
  })
  return textArr.join("")
}

console.log(solution("커피 3,500원", "350")) // '커피 <mark>3,50</mark>0원'
console.log(solution("샌드위치 2,350원", "350")) // '샌드위치 2,<mark>350</mark>원'
