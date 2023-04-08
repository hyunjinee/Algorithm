//키를 회전하는 함수
const rotationKey = (key) => {
  const len = key.length
  const ret = Array.from(Array(len), () => Array(len).fill(null))
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      ret[i][j] = key[len - j - 1][i]
    }
  }
  return ret
}

//답인지 검사하는 함수
const isAnswer = (newLock, len) => {
  for (let i = len; i < len * 2; i++) {
    for (let j = len; j < len * 2; j++) {
      if (newLock[i][j] !== 1) {
        return false
      }
    }
  }
  return true
}

const solution = (key, lock) => {
  let answer = true
  const len = lock.length
  const arr = Array.from(Array(len * 3), () => Array(len * 3).fill(null))

  for (let i = len; i < len * 2; i++) {
    for (let j = len; j < len * 2; j++) {
      arr[i][j] = lock[i - len][j - len]
    }
  }
  //키를 회전 시키면서 탐색
  for (let i = 0; i < 4; i++) {
    key = rotationKey(key, i)
    //키를 이동시키면서 탐색
    for (let j = 0; j < arr.length - key.length; j++) {
      for (let k = 0; k < arr[0].length - key[0].length; k++) {
        const newLock = arr.map(function (arr) {
          return arr.slice()
        })
        for (let m = 0; m < key.length; m++) {
          for (let n = 0; n < key.length; n++) {
            if (newLock[j + m][k + n] === 1 && key[m][n] === 1) {
              //키가 둘다 1이면 2로바꿈 -> 답이 될수 없음
              newLock[j + m][k + n] = 2
            } else if (newLock[j + m][k + n] === 1 && key[m][n] === 0) {
              newLock[j + m][k + n] = 1
            } else {
              newLock[j + m][k + n] = key[m][n]
            }
          }
        }
        if (isAnswer(newLock, len)) {
          return true
        }
      }
    }
  }
  return false
}
