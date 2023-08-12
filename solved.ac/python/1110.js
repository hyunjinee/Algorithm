let fs = require("fs");
let input = fs.readFileSync("./dev/stdin").toString().split(" ");

let num = Number(input);

let cycle = 0;
let temp = num;
let step = 0;
let isNotSame = true;

while (isNotSame) {
  cycle++;

  if (temp < 10) {
    step = temp % 10;
  } else {
    step = Math.floor(temp / 10) + (temp % 10);
  }
  /*
  step = temp % 10;
  if (temp >= 10) {
    step += Math.floor(temp / 10);
  }
  */

  temp = (temp % 10).toString() + (step % 10).toString();
  temp = Number(temp);

  if (temp === num) {
    isNotSame = false;
  }
}

console.log(cycle);
