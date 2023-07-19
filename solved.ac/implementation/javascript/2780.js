const input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n").slice(1).map(Number)

let num = Math.max(...input)
let dp = new Array(10).fill(1)
let result = [0, 10]
for (let i = 2; i <= num; i++) {
  let arr = []
  let sum = 0
  arr[0] = dp[7] % 1234567
  arr[1] = (dp[2] + dp[4]) % 1234567
  arr[2] = (dp[1] + dp[3] + dp[5]) % 1234567
  arr[3] = (dp[2] + dp[6]) % 1234567
  arr[4] = (dp[1] + dp[5] + dp[7]) % 1234567
  arr[5] = (dp[2] + dp[4] + dp[6] + dp[8]) % 1234567
  arr[6] = (dp[3] + dp[5] + dp[9]) % 1234567
  arr[7] = (dp[4] + dp[8] + dp[0]) % 1234567
  arr[8] = (dp[5] + dp[7] + dp[9]) % 1234567
  arr[9] = (dp[6] + dp[8]) % 1234567
  dp = [...arr]
  for (let j = 0; j < 10; j++) {
    sum += arr[j]
  }
  result.push(sum % 1234567)
}

let results = []
for (let i = 0; i < input.length; i++) {
  results.push(result[input[i]])
}

console.log(results.join("\n"))
