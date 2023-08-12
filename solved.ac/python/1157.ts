import fs from 'fs'

let input: string = fs.readFileSync('/dev/stdin', 'utf8')

input = input.toUpperCase()

function solution(input: string) : string {
  const answer: number[] = new Array(26).fill(0)
  for (let i = 0; i < input.length; i++) {
    answer[input.charCodeAt(i) - 65]++
  }
  const max : number = Math.max(...answer)
  return answer.filter(v => v === max).length === 1 
  ? String.fromCharCode(answer.findIndex(v => v=== max) + 65)
  : '?'
}

console.log(solution(input))