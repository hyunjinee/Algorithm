const fs = require("fs")
let input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")
// console.log(input)
solution(input)
function solution(testcaseArray) {
  const sentenceArr = testcaseArray
    .filter((p) => p !== "*")
    .map((p) => p.toLowerCase())

  sentenceArr.forEach((sentence) => {
    const firstCharArr = sentence.split(" ").map((w) => w.substr(0, 1))
    const uniqueArr = [...new Set(firstCharArr)]
    if (uniqueArr.length === 1) {
      console.log("Y")
    } else {
      console.log("N")
    }
  })
}

//         const uniqArr = [...new Set(firstCharArr)]
//         if (uniqArr.length === 1) {
//             console.log('Y')
//         } else {
//             console.log('N')
//         }
//     })
// }
