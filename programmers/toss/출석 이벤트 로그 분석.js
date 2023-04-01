function solution(ids, days) {
  const answer = []
  const users = new Set()

  ids.forEach((id) => users.add(id))

  const usersArr = Array.from(users)

  console.log(usersArr)

  usersArr.forEach((user) => {
    const userDays = new Set()

    ids.forEach((id, index) => {
      if (id === user) {
        userDays.add(days[index])
      }
    })

    if (userDays.size >= 3) {
      answer.push(user)
    }
  })

  answer.sort()
  console.log(answer)
  return answer
}

console.log(
  solution(
    [3, 1, 2, 3, 3, 1, 1, 3],
    ["월", "월", "화", "목", "수", "수", "일", "일"]
  )
)

console.log(solution([1, 1, 1], ["월", "월", "화"]))
// 3일 이상 출석한 사람들의 목록을 계산
