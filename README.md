# JavaScript Patterns

## N \* N 배열 회전

```js
const arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]
function rotate(arr) {
  const N = arr.length
  const result = Array.from(Array(N), () => Array(N).fill(0))

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      result[j][N - 1 - i] = arr[i][j]
    }
  }

  return result
}

console.log(rotate(arr))
```

## toString(2)을 사용해 숫자를 이진수로 변환

```js
const count = 10
console.log(count.toString(2)) // 1010
```

## 연속된 문자열 만들기

```js
Array(5)
  .fill()
  .map((_, i) => String.fromCharCode(65 + i))
// [ 'A', 'B', 'C', 'D', 'E' ]
Array(5)
  .fill()
  .map((v, i) => String.fromCharCode(97 + i))
// [ 'a', 'b', 'c', 'd', 'e' ]
```

## 문자열 길이 채우기

```js
"f".padStart(3) // "  f"
"f".padStart(3, "0") // "00f"
"f".padEnd(3, "0") // "f00"
```

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fhyunjinee%2FAlgorithm&count_bg=%23262382&title_bg=%233E2ABA&icon=mediafire.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
