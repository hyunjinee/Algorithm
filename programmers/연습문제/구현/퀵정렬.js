function quickSort(array) {
  if (array.length < 2) {
    return array
  }

  const pivot = [array[0]]
  const left = []
  const right = []

  for (let i = 1; i < array.length; i++) {
    if (array[i] < pivot) {
      left.push(array[i])
    } else if (array[i] > pivot) {
      right.push(array[i])
    } else {
      pivot.push(arra[i])
    }
  }

  console.log(`left = ${left} pivot = ${pivot} right = ${right}`)

  return quickSort(left).concat(pivot, quickSort(right))
}

console.log(quickSort([5, 3, 7, 1, 9]))
