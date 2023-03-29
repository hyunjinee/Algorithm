function solution(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    let temp = Infinity

    for (let j = i + 1; j < arr.length; j++) {
      temp = Math.min(temp, arr[j])
    }

    const minIndex = arr.indexOf(temp, i + 1)

    if (arr[i] > arr[minIndex]) {
      const temp = arr[i]
      arr[i] = arr[minIndex]
      arr[minIndex] = temp
    }
  }

  return arr
}

console.log(solution([3, 4, 5, 2, 6, 7, 9, 1, 8, 0]))

// 선택정렬은 점차 정렬의 범위를 넓혀간다고 생각할 수 있다.
// 배열의 첫 번째 자리에는 배열 요소 중 가장 작은 요소가 들어가면 된다. 그리고 두번쨰 잘에는 두번째로 작은 요소가 들어가면 된다.

function selectionSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    let minIndex = i
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[minIndex] > arr[j]) {
        minIndex = j
      }

      if (minIndex !== i) {
        ;[arr[i], arr[minIndex]] = [arr[minIndex], arr[i]]
      }
    }
  }

  return arr
}

console.log(selectionSort([3, 4, 5, 2, 6, 7, 9, 1, 8, 0]))

// 이중 선택 정렬(Double Selection Sort)
// 최소 최대 정렬이라고도 부르는 이중 선택 정렬은 선택 정렬에서 최솟값을 찾는 괒어에서 최댓값까지 함께 찾아 최솟값과 최댓값을 동시에
// 정렬한다면 시간이 반으로 줄지 않을까라는 아이디어로 등장한 정렬 알고리즘입니다. 이중 선택 정렬은은 선택 정렬이 순회하면서
// 최솟값을 찾는 과정에 최댓값까지 같이 찾은 다음 최솟값은 앞쪽에 최댓값은 뒤쪽에 배치하면서 정렬을 진행합니다.

function doubleSelectionSort(arr) {
  let start = 0
  let end = arr.length

  while (start < end) {
    let min = start
    let max = end

    for (let i = start; i < end; i++) {
      if (arr[min] > arr[i]) {
        min = i
      }
      if (arr[max] < arr[i]) {
        max = i
      }
    }

    if (start !== min) {
      ;[arr[start], arr[min]] = [arr[min], arr[start]]
    }

    if (end !== max) {
      ;[arr[end], arr[max]] = [arr[max], arr[end]]
    }

    start++
    end--
  }
}
