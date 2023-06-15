const numPrimeArrangements = function (n) {
  const mod = 10 ** 9 + 7
  let primes = 0,
    nonPrimes = 0
  let res = 1
  for (let i = 1; i <= n; i++) {
    if (isPrime(i)) res *= ++primes
    else res *= ++nonPrimesk
    res = res % mod
  }
  return res
  // Time Complexity: O(n^(3/2))
  // Space Complexity: O(1)
}

const isPrime = function (n) {
  if (n <= 1) return false
  if (n <= 3) return true
  let i = 2
  while (i <= Math.sqrt(n)) {
    if (n % i == 0) return false
    i++
  }
  return true
}
