const fs = require("fs")
let input = fs.readFileSync("./dev/stdin").toString().trim()
temp = ["pi", "ka", "chu"]
for (let i = 0; i < 3; i++) {
  input = input.replaceAll(temp[i], "*")
}
let flag = true
for (let i = 0; i < input.length; i++) {
  // console.log(input[i].charCodeAt(), "a".charCodeAt())
  if (
    input[i].charCodeAt() >= "a".charCodeAt() &&
    input[i].charCodeAt() <= "z".charCodeAt()
  ) {
    console.log("NO")
    flag = false
    break
  }
}
if (flag) {
  console.log("YES")
}
