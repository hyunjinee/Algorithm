const solution = (str1, str2) => {
  //각각의 원소 쌍을 구하는 과정 Set으로 구현할 수 없어서 Array를 사용했다.
  str1 = str1.toUpperCase()
  str2 = str2.toUpperCase()
  const arr1 = new Array()
  const arr2 = new Array()

  //이부분이 str1과 str2가 겹치므로 함수로 따로 뺐어도 됐을 것 같다.
  for (let i = 0; i < str1.length - 1; i++) {
    const str = str1.slice(i, i + 2)
    if (str[0] >= "A" && str[0] <= "Z" && str[1] >= "A" && str[1] <= "Z") {
      arr1.push(str)
    }
  }
  for (let i = 0; i < str2.length - 1; i++) {
    const str = str2.slice(i, i + 2)
    if (str[0] >= "A" && str[0] <= "Z" && str[1] >= "A" && str[1] <= "Z") {
      arr2.push(str)
    }
  }

  //교집합과 합집합을 구하는 과정
  const intersection = []
  const union = []
  for (let i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) >= 0) {
      intersection.push(arr1.splice(arr1.indexOf(arr2[i]), 1))
    }
    union.push(arr2[i])
  }

  for (let i = 0; i < arr1.length; i++) {
    union.push(arr1[i])
  }
  if (intersection.length === 0 && union.length === 0) {
    return 65536
  }
  return parseInt(65536 * (intersection.length / union.length))
}
