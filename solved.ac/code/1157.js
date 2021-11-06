const fs = require('fs')
let input = fs.readFileSync('./dev/stdin', 'utf8')
input= input.toUpperCase()




function solution(input){
  const answer = new Array(26).fill(0)
  

  for (let i = 0 ; i< input.length ; i++){
    answer[input.charCodeAt(i)-65]++
  }
  const max = Math.max(...answer)
  return answer.filter(v => v === max).length === 1 
  ? String.fromCharCode(answer.findIndex(v => v === max) + 65)
  : '?'
}

console.log(solution(input))

// // 
// console.log(input)
// // 가장 많이 사용된 알파벳은 뭘까?
// let a = {}
// // console.log(input[0])
// for (let i = 0 ; i < input.length ; i++){
//   if (a[input[i]]) {
//     a[input[i]]++
//   }else {
//     a[input[i]] = 1
//   }
// }
// // console.log(Object.values(a))
// // console.log(Object.values(a))
// // console.log(Math.max(...Object.values(a)))
// max_value = Math.max(...Object.values(a))
// let count = 0
// for (let key in a) {
//   if (a[key] === max_value) {
//     // console.log(key)
//     count++
//   }
// }

// if (count > 1) {
//   console.log('?')
// }else {
//   // console.log(Object.keys(a)[Object.values(a).indexOf(max_value)])
//   console.log(Object.keys(a)[Object.values(a).indexOf(max_value)])
// }
// console.log()