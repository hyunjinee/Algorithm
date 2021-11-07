const fs = require('fs')


let input = fs.readFileSync('./dev/stdin', 'utf8')

input = input.split('\r\n')

let index = 1

for (let i = 0 ; i < parseInt(input[0]); i++) {
  let ans = []
  let num = parseInt(input[index])
  let temp = num
  if (!num) break


  for (let j = 2 ; j <= num; j++) {
    while ( num % j == 0 ) {
      ans.push(j)
      num = num / j
    }
  }
  for (let k = 2 ; k <= temp; k++) {
    if (ans.indexOf(k) != -1) {
      let l = ans.filter(v => v == k).length
      console.log(`${k} ${l}`)
    }
  }


  index++
}
