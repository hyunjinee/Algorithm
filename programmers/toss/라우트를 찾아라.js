function parse(route, path) {
  if (!route.includes("[")) {
    return {
      matches: route === path,
      params: {},
    }
  }

  if (route.includes("[")) {
    const routeArr = route.split("/")
    const pathArr = path.split("/")

    console.log(routeArr, pathArr)

    const idxArr = []
    const params = []
    routeArr.forEach((x, i) => {
      if (x.startsWith("[")) {
        idxArr.push(i)
      }
    })

    idxArr.forEach((x, i) => {
      if (pathArr[x]) {
        params.push([routeArr[x].slice(1, -1), pathArr[x]])
      }
    })

    console.log(idxArr)
    console.log(params)

    if (routeArr.length !== pathArr.length) {
      return {
        matches: false,
      }
    }

    const p = {}

    for (const [a, b] of params) {
      p[a] = b
    }

    return {
      matches: true,
      params: p,
    }
  }
  return {
    matches: false,
  }
}

function solution(route, path) {
  const result = parse(route, path)

  return JSON.stringify(result)
}

console.log(solution("/about", "/about"))
console.log(solution("/service/[id]", "/service/1"))
console.log(solution("/about", "/"))
console.log(
  solution("/service/[id]/deployment/[deploymentId]", "/service/1/deployment/9")
)
