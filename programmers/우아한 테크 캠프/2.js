// 공휴일과 사용할 수 있는 연차의 개수가 주어졌을 때,
// 가장 길게 떠날 수 있는 날은 며칠인지 계산하려고 한다.

function solution(leave, day, holidays) {
  // leave : 1 ~ 30 이하의 정수
  // day: 길이 3인 알파벳 대문자로 구성된 문자열로, 7가지중 하나.
  // holidays: 1~30 정수 배열
  if (leave == 30) {
    console.log(30)
    return
  }
  const days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

  let dayStartIndex = days.indexOf(day)
  const calendar = {}

  for (let i = 1; i <= 30; i++) {
    calendar[i] = days[dayStartIndex % 7]
    dayStartIndex = (dayStartIndex + 1) % 7
  }

  let maximumHolidays = 0

  for (let i = 1; i <= 30; i++) {
    let tempHolidayCount = 0,
      tempLeaveCount = leave
    for (let j = i; j <= 30; j++) {
      if (holidays.indexOf[j] !== undefined) {
        tempHolidayCount++
        continue
      }

      if (calendar[j] === "SAT" || calendar[j] === "SUN") {
        tempHolidayCount++
        continue
      }

      if (tempLeaveCount <= 0) {
        let today = calendar[j]
        if (j <= 28) {
          let nextDay = calendar[j + 1]
          let nextnextDay = calendar[j + 2]
          if (nextDay == "SAT" || nextDay == "SUN") {
            tempHolidayCount++
          } else {
            break
          }
          if (nextnextDay == "SAT" || nextnextDay == "SUN") {
            tempHolidayCount++
          } else {
            break
          }
        } else if (j == 29) {
          let nextDay = calendar[j + 1]
          if (nextDay == "SAT" || nextDay == "SUN") {
            tempHolidayCount++
          } else {
            break
          }
        } else if (j == 30) {
          if (today == "SAT" || today == "SUN") {
            tempHolidayCount++
          } else {
            break
          }
        }
      }

      if (calendar[j] != "SAT" && calendar[j] != "SUN") {
        tempLeaveCount--
        tempHolidayCount++
      }
    }

    maximumHolidays = Math.max(maximumHolidays, tempHolidayCount)
    console.log(maximumHolidays)
  }

  console.log(maximumHolidays)
}

solution(4, "FRI", [6, 21, 23, 27, 28]) // 10
// solution(3, "SUN", [2,6,17, 29] ) // 8
// solution(30, "MON", [1, 2, 3, 4, 28, 29, 30]) // 30
