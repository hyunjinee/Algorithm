/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
const getHint = function (secret, guess) {
  let y = 0
  let x = 0

  const 찜 = []

  for (let i = 0; i < Math.max(secret.length, guess.length); i++) {
    if (secret[i] === guess[i]) {
      x++

      찜.push(i)
    }
  }

  const secretMap = {}

  for (let i = 0; i < secret.length; i++) {
    if (찜.includes(i)) {
      continue
    }

    if (secretMap[secret[i]] === undefined) {
      secretMap[secret[i]] = 1
    } else {
      secretMap[secret[i]]++
    }
  }

  for (let i = 0; i < guess.length; i++) {
    if (찜.includes(i)) {
      continue
    }

    if (secretMap[guess[i]] > 0) {
      y++
      secretMap[guess[i]]--
    }
  }

  return `${x}A${y}B`
}
