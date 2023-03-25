function solution(priorities, location) {
  priorities = priorities.map((p, i) => [p, i])

  let counter = 0
  while (priorities.length) {
    const next = priorities.shift()
    if (next) {
      const priority = next[0]
      let flag = true
      priorities.forEach((p, i) => {
        if (p[0] > priority) {
          flag = false
        }
      })
      if (flag) {
        counter++

        if (next[1] === location) {
          return counter
        }
      } else {
        priorities.push(next)
      }
    } else {
      break
    }
  }
}
solution([2, 1, 3, 2], 2) // 1
// 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄한다.
// 그렇기 떄문에 중요한 문서가 나중에 인쇄될 수 있다.

// 이러한 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했다.

// 1. 인쇄 대기목록의 가장 앞에 있는 문서 (J)를 대기목록에서 꺼낸다.
// 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한개라도 존재하면 J를 대기목록의 가장 마지막에 넣는다.
// 3. 그렇지 않으면 J를 인쇄한다.

// priorities: 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열
// location: 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 인덱스
