var fs = require("fs")
var line = fs.readFileSync("/dev/stdin", "utf8")
var S = line[0]
console.log(pika(line))
// console .log( ( t => t .match( /^(pi|ka|chu)*(\n|$)/ ) )( S ) );
function pika(t) {
  return t.match(/^(pi|ka|chu)*?(\s|$)/) ? "YES" : "NO"
}
