function solution(leave, day, holidays) {
  // leave 연차의 개수
  // day 첫날을 나타내는 요일
  // holidays 공휴일을 나타내는 정수 배열
  if (leave == 30) {
    console.log(30)
    return
  }

  const days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
  const calendar = {}

  let dayStartIndex = days.indexOf(day)
  let maximumHolidays = 0

  for (let i = 1; i <= 30; i++) {
    calendar[i] = days[dayStartIndex % 7]
    dayStartIndex = (dayStartIndex + 1) % 7
  }

  for (let i = 0; i <= 30; i++) {
    let tempHolidayCount = 0
    let tempLeaveCount = leave

    for (let j = i; j <= 30; j++) {
      if (holidays.includes(j)) {
        tempHolidayCount++
        continue
      }

      if (calendar[j] === "SAT" || calendar[j] === "SUN") {
        tempHolidayCount++
        continue
      }

      if (tempLeaveCount) {
        tempLeaveCount--
        tempHolidayCount++
        continue
      }

      if (tempLeaveCount == 0) {
        for (let k = j; k <= 30; k++) {
          let temp = calendar[k]

          if (temp == "SAT" || temp == "SUN") {
            tempHolidayCount++
          } else if (holidays.includes(k)) {
            tempHolidayCount++
          } else {
            break
          }
        }
        break
      }
    }
    maximumHolidays = Math.max(tempHolidayCount, maximumHolidays)
  }
  console.log(maximumHolidays)
}

// solution(4, "FRI", [6, 21, 23, 27, 28]) // 10
solution(3, "SUN", [2, 6, 17, 29]) // 8
// solution(30, "MON", [1, 2, 3, 4, 28, 29, 30]) // 30
