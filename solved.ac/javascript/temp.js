const person = {
  name: "Lee",
  sayHello: function () {
    console.log(`hello my name is ${this.name}`)
  },
}

console.log(typeof person) // object
console.log(person) // { name :'Lee', sayHello: [Function: sayHello] }

const empty = {}
console.log(typeof empty) // object

const person2 = {
  firstName: "hyunjin", // 식별자 네이밍 규칙을 준수하는 프로퍼티 키
  "last-name": "lee", // 식별자 네이밍 규칙을 준수하지 않는 프로퍼티 키
}
console.log(person2) // { firstName: 'hyunjin', last-name: 'lee' }
