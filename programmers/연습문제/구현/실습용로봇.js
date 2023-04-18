function solution(command) {
  var answer = []
  let [x, y] = [0, 0]

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]
  let direction = 0
  for (let i = 0; i < command.length; i++) {
    if (command[i] === "R") {
      direction = (direction + 1) % 4
    } else if (command[i] === "L") {
      if (direction - 1 >= 0) {
        direction = (direction - 1) % 4
      } else {
        direction = 3
      }
    } else if (command[i] === "G") {
      x += dx[direction]
      y += dy[direction]
    } else if (command[i] === "B") {
      x -= dx[direction]
      y -= dy[direction]
    }
  }

  return [x, y]
}
