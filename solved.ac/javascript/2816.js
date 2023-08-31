let fs = require("fs")
let input = fs.readFileSync("./dev/stdin").toString().split("\n")
let N = parseInt(input.shift())

let index1 = input.indexOf("KBS1")
let index2 = input.indexOf("KBS2")
index2 = index1 > index2 ? ++index2 : index2

let result = ""

for (let i = 0; i < index1; i++) {
  result += "1"
}

for (let i = 0; i < index1; i++) {
  result += "4"
}

for (let i = 0; i < index2; i++) {
  result += "1"
}

for (let i = 0; i < index2 - 1; i++) {
  result += "4"
}

console.log(result)
// const fs = require("fs")
// const inputs = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
// const n = +inputs.shift()
// const channels = inputs
// const kbs1 = channels.indexOf("KBS1")
// const kbs2 = channels.indexOf("KBS2")

// let ans = ""
// let pointer = 0

// while (channels[0] !== "KBS1") {
//   if (channels[pointer] === "KBS1") {
//     ans += "4"
//     ;[channels[pointer], channels[pointer - 1]] = [channels[pointer - 1], channels[pointer]]
//     // console.log(channels)
//     pointer -= 1

//     if (channels[0] === "KBS1") break
//   }

//   ans += "1"
//   pointer += 1
// }

// while (channels[1] !== "KBS2") {
//   if (channels[pointer] === "KBS2") {
//     ans += "4"
//     ;[channels[pointer], channels[pointer - 1]] = [channels[pointer - 1], channels[pointer]]
//     // console.log(channels)
//     pointer -= 1

//     if (channels[1] === "KBS2") break
//   }

//   ans += "1"
//   pointer += 1
// }

// console.log(ans)
