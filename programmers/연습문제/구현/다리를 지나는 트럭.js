function solution(bridgeLength, weight, truckWeights) {
  let timer = 0
  let truckOnBridge = new Array(bridgeLength).fill(0)
  let totalWeight = 0
  let currentTruck = truckWeights.shift()

  truckOnBridge.unshift(currentTruck)
  truckOnBridge.pop()
  console.log(truckOnBridge)
  totalWeight += currentTruck
  timer += 1

  while (totalWeight) {
    totalWeight -= truckOnBridge.pop()
    currentTruck = truckWeights.shift()

    if (currentTruck + totalWeight <= weight) {
      truckOnBridge.unshift(currentTruck)
      totalWeight += currentTruck
    } else {
      truckOnBridge.unshift(0)
      truckWeights.unshift(currentTruck)
    }

    timer++
  }

  return timer
}

solution(2, 10, [7, 4, 5, 6]) // 8
