const map = new Map()

map.set("name", "crong")
map.set("age", 10)

console.log(map.keys())

for (let key of map.keys()) {
  console.log(key)
}

for (let value of map.values()) {
  console.log(value)
}

for (let [a, b] of map.entries()) {
  console.log(a, b)
}

for (let [a, b] of map) {
  console.log(a, b)
}

console.log(NaN !== NaN)
