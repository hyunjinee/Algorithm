function createQueryString(object) {
  let result = ""

  for (const [key, value] of Object.entries(object)) {
    if (value === null) {
      continue
    }

    if (Array.isArray(value)) {
      if (result.length === 0) {
        result += `${key}=${value[0]}`

        for (let i = 1; i < value.length; i++) {
          result += `&${key}=${value[i]}`
        }
      } else {
        result += value.reduce((acc, cur) => {
          return `${acc}&${key}=${cur}`
        }, "")
      }

      continue
    }

    if (result.length > 0) {
      result += "&"
    }

    result += `${key}=${value}`
  }

  console.log(result)
  console.log(result.length > 0 ? `?${result}` : "")
  return result.length > 0 ? `?${result}` : ""
}

function solution(input) {
  const object = JSON.parse(input)
  if (Object.keys(object).length === 0) return ""

  console.log(Object.entries(object))

  const answer = createQueryString(object)
  return answer
}

console.log(solution('{"foo":"bar", "baz": null}'))
console.log(
  solution('{"foo":false, "bar":[1,2,3], "baz": null, "foobar": 3333}')
)
console.log(solution("{}"))
console.log(solution('{"foo":"bar", "enabled": true}'))
console.log(solution('{"foo": [1,2,3]}'))
