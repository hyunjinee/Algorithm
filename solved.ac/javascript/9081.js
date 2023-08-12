const fs = require("fs")
const inputData = fs
  .readFileSync(0, "utf8")
  .toString()
  .trim()
  .split("\n")
  .slice(1)
  .map((item) => item.split(""))

let result = ""
inputData.forEach((item) => {
  let arr = item
  let i = arr.length - 2
  while (i >= 0 && arr[i] >= arr[i + 1]) {
    i--
  }
  if (i === -1) {
    result = item.join("")
    return console.log(result)
  }
  let j = arr.length - 1
  while (j >= 0 && arr[i] >= arr[j]) {
    j--
  }
  let temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
  result =
    arr.slice(0, i + 1).join("") +
    arr
      .slice(i + 1)
      .sort((a, b) => a.localeCompare(b))
      .join("")
  console.log(result)
})

// const fs = require("fs")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
// const t = input.shift()

// for (let i = 0; i < t; i++) {
//   console.log(findWord(input[i]))
// }

// function findWord(word) {
//   const arr = word.split("").sort((a, b) => a.localeCompare(b))
//   const visited = Array(arr.length).fill(false)
//   const keep = []

//   let flag = false
//   let result

//   backTracking([])

//   return result

//   function backTracking(curr) {
//     if (flag && curr.length === arr.length) {
//       result = curr.join("")

//       return
//     }
//     if (curr.length === arr.length && word === curr.join("")) {
//       console.log(curr.join(""), "what")
//       flag = true
//       return
//     }

//     for (let i = 0; i < arr.length; i++) {
//       if (visited[i]) {
//         continue
//       }

//       visited[i] = true
//       backTracking([...curr, arr[i]])
//       visited[i] = false
//     }
//   }
// }
// const fs = require("fs")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
// const t = input.shift()

// for (let i = 0; i < t; i++) {
//   console.log(findWord(input[i]))
// }

// function findWord(word) {
//   const arr = word.split("").sort((a, b) => a.localeCompare(b))
//   const visited = Array(arr.length).fill(false)
//   const keep = []

//   backTracking([])

//   const index = keep.indexOf(word)

//   return keep[index + 1]

//   function backTracking(curr) {
//     if (curr.length === arr.length) {
//       keep.push(curr.join(""))
//     }

//     for (let i = 0; i < arr.length; i++) {
//       if (visited[i]) {
//         continue
//       }

//       visited[i] = true
//       backTracking([...curr, arr[i]])
//       visited[i] = false
//     }
//   }
// }
