function solution(today, terms, privacies) {
  const answer = []
  const map = new Map()

  for (let term of terms) {
    const [a, b] = term.split(" ")
    map.set(a, Number(b))
  }

  const [tYear, tMonth, tDay] = today.split(".").map(Number)

  let i = 0
  for (let privacy of privacies) {
    i++
    const [str, type] = privacy.split(" ")
    const long = map.get(type)
    let [year, month, day] = str.split(".").map(Number)
    console.log(year, month, day)

    day = day + long * 28 - 1

    if (day > 28) {
      month = month + Math.floor(day / 28)
      day = day % 28
    }

    if (day === 0) {
      day = 28
      month = month - 1
      if (month === 0) {
        month = 12
        year = year - 1
      }
    }

    console.log(year, month, day)
    if (month > 12) {
      year = year + Math.floor(month / 12)
      month = month % 12
    }
    console.log(year, month, day)

    // if (month === 12) {
    //   month = 1
    //   year = year + 1
    // }
    console.log(year, month, day)

    if (month === 0) {
      month = 12
      year = year - 1
    }

    if (tYear > year) {
      answer.push(i)
      continue
    }

    if (tYear < year) {
      continue
    }

    if (tYear === year && tMonth > month) {
      answer.push(i)
      continue
    }

    if (tYear === year && tMonth === month && tDay > day) {
      answer.push(i)
      continue
    }

    console.log(year, month, day)
  }
  console.log(answer)
  return answer
}

// solution("2021.12.08", ["A 18"], ["2020.06.08 A"])

// solution("2019.01.01", ["B 12"], ["2017.12.21 B"])

// solution("2022.12.08", ["A 6"], ["2022.06.08 A"])
solution("2021.12.08", ["A 18"], ["2020.06.08 A"])
// "2022.12.08", ["A 6"], ["2022.06.08 A"], [1]
// "2021.12.08", ["A 18"], ["2020.06.08 A"], [1]
