// 1~4번까지 150분이면 4로 나누면 한개에 35분정도에 풀어야한다.
// 12: 20분 시작 4번

// 모든 칸이 동일한 크기의 작은 정삼각형으로 이루어진 모양의 격자가 있다. 각 칸은 빨간색또는 파란색으로 색칠
// 당신은 이 격자에서 다음과 같은 규칙으로 움직인다.

// 어떤 칸에 입장했을 때 해당 칸의 색이 빨간색이라면 우회전을, 파란색이라면 좌해전을 해서 나간다.
// 다음 그림은 크기가 2인 격자가 색칠되어있고 입장했다가 퇴장하는 경로 6가지를 나타낸 것이다.
// 위 격자에서 가장 많은 칸을 거치는 경로는 3개의 칸을 거친다는 것을 알 수 있따.

// ["B", "RRB"] 3
// ["R", "BBB"]

// 삼각형 격자의 색깔 분포를 나타내는 문자열 배열 grid가 매개변수로 주어진다. 주어진 격자에 입장했다가 퇴장하는 경로들 중에서,
// 가장 많은 칸을 거치는 경로를 찾아, 그 경로가 거치는 칸의 개수를 return 하도록 solution함수를 완성하자.
// 이 때 한번 지나간 칸을 다시한번 지나가는 것도 중복한다.

function solution(grid) {
  var answer = 0
  const nextD = new Map([
    [
      "NR",
      new Map([
        [
          "L",
          new Map([
            ["R", "D"],
            ["B", "L"],
          ]),
        ],
        [
          "R",
          new Map([
            ["R", "R"],
            ["B", "D"],
          ]),
        ],
        [
          "D",
          new Map([
            ["R", "L"],
            ["B", "R"],
          ]),
        ],
      ]),
    ],
    [
      "RV",
      new Map([
        [
          "L",
          new Map([
            ["R", "L"],
            ["B", "D"],
          ]),
        ],
        [
          "R",
          new Map([
            ["R", "D"],
            ["B", "R"],
          ]),
        ],
        [
          "D",
          new Map([
            ["R", "R"],
            ["B", "L"],
          ]),
        ],
      ]),
    ],
  ])
  const dir = new Map([
    [
      "NR",
      new Map([
        //정방향
        [
          "L",
          new Map([
            ["R", [1, 1]],
            ["B", [0, 1]],
          ]),
        ],
        [
          "R",
          new Map([
            ["R", [0, -1]],
            ["B", [1, 1]],
          ]),
        ],
        [
          "D",
          new Map([
            ["R", [0, 1]],
            ["B", [0, -1]],
          ]),
        ],
      ]),
    ],
    [
      "RV",
      new Map([
        //거꾸로
        [
          "R",
          new Map([
            ["R", [-1, -1]],
            ["B", [0, -1]],
          ]),
        ],
        [
          "L",
          new Map([
            ["R", [0, 1]],
            ["B", [-1, -1]],
          ]),
        ],
        [
          "D",
          new Map([
            ["R", [0, -1]],
            ["B", [0, 1]],
          ]),
        ],
      ]),
    ],
  ])
  for (let i = 0; i < grid.length; i++) {
    find(i, 0, "L", 0)
    find(i, grid[i].length - 1, "R", 0)
    if (i == grid.length - 1) {
      for (let j = 1; j < parseInt(grid[i].length / 2); j++) {
        find(i, j * 2, "D", 0)
      }
    }
  }
  function find(a, b, d, count) {
    // x, y, dir
    if (a < 0 || a >= grid.length || b < 0 || b >= grid[a].length) {
      answer = Math.max(answer, count)
      return
    }
    let color = grid[a].charAt(b)
    let now_d = ""
    if (b % 2 == 0) {
      now_d = "NR"
    } else {
      now_d = "RV"
    }
    var dirs = dir.get(now_d).get(d).get(color)
    var nextDir = nextD.get(now_d).get(d).get(color)
    find(a + dirs[0], b + dirs[1], nextDir, count + 1)
  }
  console.log(answer)
  return answer
}

solution(["B", "RRB"]) // 3
// solution(["R", "BBB", "RBRBR"]) // 7
// solution(["R", "RRR", "RBBBB", "BRRRBRR"]) // 15

// x B x
// R R B
