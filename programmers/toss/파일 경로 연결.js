function solution(paths) {
  let result = ""

  for (const path of paths) {
    if (result.length === 0 && path.startsWith("/")) {
      result += path
      continue
    }

    if (result.length === 0 && !path.startsWith("/") && !path.startsWith(".")) {
      result += `/${path}`
      continue
    }

    if (result.length > 0 && path !== "." && path !== ".." && path !== "...") {
      result += `/${path}`
      continue
    }

    if (path === ".") {
      continue
    }

    if (result.length > 0 && path === "..") {
      result = result.split("/").slice(0, -1).join("/")
      continue
    }

    if (result.length > 0 && path === "...") {
      result = result.split("/").slice(0, -2).join("/")
      continue
    }

    if (result.includes("./")) {
      result = result.replace("./", "")
      continue
    }
  }

  if (result.includes("./")) {
    result = result.replace("./", "")
  }
  return result
}

// . 는 현재 경로
// .. 은 부모 경로
// ...는 부모의 부모 경로
// solution에서는 파일 경로들을 연결하여 ., .., ...가 없는 형태로 반환

console.log(solution(["/foo", "bar", "baz/asdf", "quux", ".."])) // /foo/bar/baz/asdf
console.log(solution(["/foo", "bar", "baz/asdf", "quux", ".."])) // /foo/bar/baz/asdf
console.log(solution(["/foo", "bar", "baz/./asdf"])) // /foo/bar/baz/asdf
console.log(solution(["/foo", "bar", "...", ".", "ab"])) // /ab
