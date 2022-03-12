const fs = require("fs")
let [a, b, c] = fs.readFileSync("/dev/stdin").toString().split(" ")

a = +a
b = +b
c = +c

console.log(`${(a + b) % c}
${((a % c) + (b % c)) % c}
${(a * b) % c}
${((a % c) * (b % c)) % c}
`)

// A,B,C = map(int,input().split())

// print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
// # sep='\n'로 줄바꿈
