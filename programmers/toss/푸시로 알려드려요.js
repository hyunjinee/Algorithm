async function solution(fetchPaper) {
  // 1초 안에 fetchPaper가 resolve되면 그대로 반환
  // 1초 안에 fetchPaper가 reject되면 reject
  // 1초 안에 fetchPaper가 resolve되지 않으면 reject
  let result
  return new Promise((resolve, reject) => {
    fetchPaper()
      .then((res) => (result = res))
      .catch((err) => reject(err))
    setTimeout(() => {
      if (result) {
        resolve(result)
      }
      reject(new Error("그 외의 경우"))
    }, 1000)
  })
}

async function fetchPaper() {
  return new Promise((res, rej) => {
    // setTimeout(() => rej("rej"), 1500)
    setTimeout(() => rej("rej"), 500)
    // setTimeout(() => res("res"), 500)
  })
}

async function test() {
  try {
    const result = await solution(fetchPaper)
    console.log(result)
  } catch (error) {
    console.log(error)
    console.log(error.message)
  }
  console.log(result)
}

test()
