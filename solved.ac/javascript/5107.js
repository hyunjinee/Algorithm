const fs = require("fs")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

let testCase = 1

while (1) {
  const graph = {}
  let ans = 0
  function dfs(name) {
    if (!name) {
      return
    }

    if (!graph[name][1]) {
      graph[name][1] = true
      dfs(graph[name][0])
    } else {
      ans++
      return
    }
  }
  const peopleCount = Number(input.shift())

  if (!peopleCount) {
    break
  }

  while (1) {
    const temp = input.shift()

    if (temp == "0" || !temp) {
      break
    }
    const [a, b] = temp.split(" ")
    graph[a] = [b, false]
  }

  for (const key in graph) {
    if (!graph[key][1]) {
      dfs(key)
    }
  }

  console.log(`${testCase} ${ans}`)

  testCase++
}

// const peopleCount = Number(input.shift())
// input.pop()
// const graph = {}

// for (const inputCase of input) {
//   const [a, b] = inputCase.split(" ")

//   if (b in graph) {

//   }
// }

// // Graph. with Direction
// const fs = require("fs")
// const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n")

// const answer = []
// let order = 1
// let index = 0

// while (index < inputs.length) {
//   const N = +inputs[index++]

//   if (N === 0) break

//   const names = inputs.slice(index, index + N)
//   const visited = Array.from({ length: N }, () => false)
//   const finished = Array.from({ length: N }, () => false)
//   const relations = {}
//   const numToName = {}
//   const nameToNum = {}

//   let count = 0
//   names.forEach((el) => {
//     const [from, to] = el.split(" ")
//     if (relations[from] === undefined) {
//       numToName[count] = from
//       nameToNum[from] = count
//       count++
//       relations[from] = []
//     }
//     relations[from].push(to)
//   })

//   const dfs = (name) => {
//     for (const next of relations[name]) {
//       const num = nameToNum[next]
//       if (visited[num] === false) {
//         visited[num] = true
//         dfs(next)
//       } else if (finished[num] === false) {
//         result++
//       }
//       finished[num] = true
//     }
//   }

//   let result = 0
//   for (let i = 0; i < N; i++) {
//     if (visited[i] === false) {
//       visited[i] = true
//       dfs(numToName[i])
//     }
//   }

//   answer.push(`${order++} ${result}`)
//   index += N
// }

// console.log(answer.join("\n"))
// import sys
// input = sys.stdin.readline

// test = 0
// while True:
//     test += 1
//     n = int(input())
//     if n == 0: break
//     part = dict()
//     people = list()
//     for _ in range(n):
//         a, b = input().split()
//         part[a] = b
//         people.append(a)
//     visited = [False] * n

//     cycle = 0
//     for i in range(n):
//         if not visited[i]:
//             visited[i] = True
//             cycle += 1
//         now = i
//         while not visited[people.index(part[people[now]])]:
//             now = people.index(part[people[now]])
//             visited[now] = True
//     print(test, cycle)
// import sys
// input = sys.stdin.readline

// def find(x) :
//     if x != parent[x] :
//         parent[x] = find(parent[x])
//     return x

// def union(x,y) :
//     x = find(x)
//     y = find(y)

//     if x < y :
//         parent[y] = x
//     else :
//         parent[x] = y

// cnt = 0
// while True :
//     n = int(input())
//     parent = [i for i in range(n + 1)]
//     mp = {}
//     cnt += 1

//     if n == 0 :
//         break

//     for _ in range(n) :
//         t1, t2 = map(str, input().split())

//         if not t1 in mp :
//             mp[t1] = len(mp) + 1
//         if not t2 in mp :
//             mp[t2] = len(mp) + 1

//         union(parent[mp[t1]], parent[mp[t2]])

//     parent = set(parent)
//     print(cnt, len(parent)-1)
