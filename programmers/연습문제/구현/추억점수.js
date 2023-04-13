function solution(name, yearning, photo) {
  const map = new Map()

  for (let i = 0; i < name.length; i++) {
    map.set(name[i], yearning[i])
  }

  return photo.map((p) => {
    let temp = 0
    p.forEach((people) => {
      if (map.get(people)) {
        temp += map.get(people)
      }
    })

    return temp
  })
}
