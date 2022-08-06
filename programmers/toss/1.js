function safelyGet(object, path) {
  const paths = path.split(".")
  let depth = 0

  function findObject(object, key) {
    const value = object[key]

    if (value) {
      return value
    }

    if (value === undefined || Object.keys(value).length === 0) {
      return value
    }

    depth += 1

    return findObject(value, paths[depth])
  }

  return findObject(object, paths[depth])
}

function solution(input, path) {
  const result = safelyGet(JSON.parse(input), path)
  console.log(result)
  if (result === undefined) {
    return "undefined"
  }
  console.log(result, "?")
  return JSON.stringify(result)
}

/**
const object1 = {
repository: undefined,
};

const object2 = {
repository: {
  readme: undefined,
},
};

const object3 = {
repository: {
  readme: {
    extension: 'md',
    content: '금융을 쉽고 간편하게',
  }
}
};

safelyGet(object2, 'repository.readme.extension')  // -> undefined
safelyGet(object2, 'repository.readme')            // -> undefined
safelyGet(object1, 'repository')                   // -> { readme: undefined }
*/
