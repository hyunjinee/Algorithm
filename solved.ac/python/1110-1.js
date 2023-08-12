let fs = require("fs");
const { type } = require("os");
let input = fs.readFileSync("./dev/stdin").toString();

// console.log(typeof input);

let num = Number(input);
// console.log(typeof num);
// console.log(num + 1);

let count = 0;
while (true) {
  let ten = num / 10;
  ten = Math.floor(ten);

  let one = num % 10;
  let total = ten + one;
  count++;
  num = (num % 10).toString() + (total % 10).toString();

  if (num == Number(input)) {
    break;
  }
}
console.log(count);
