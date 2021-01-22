let fs = require("fs");
let input = fs.readFileSync("./dev/stdin").toString().split("\n");
// for (i in input) {
//   console.log(input[i]);
// }
players = [];
for (let i = 1; i <= input[0]; i++) {
  players.push(input[i].slice(0, -1));
}

//console.log(players);
p = {};

for (let i = 0; i < players.length; i++) {
  p[players[i][0]] = 0;
}
for (let i = 0; i < players.length; i++) {
  p[players[i][0]] += 1;
}
letsgo = [];
// console.log(p);
for (item in p) {
  //   console.log(item);
  if (p[item] > 4) {
    letsgo.push(item);
  }
}
letsgo.sort();
// console.log(letsgo);
if (letsgo.length > 0) console.log(letsgo.join(""));
else {
  console.log("PREDAJA");
}
