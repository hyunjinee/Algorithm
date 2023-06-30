const simplifyPath = function (path) {
  const stack = []

  path = path.split("/")

  // console.log(path)

  for (let i = 0; i < path.length; i++) {
    if (path[i] == "." || path[i] == "") continue
    if (path[i] == "..") stack.pop()
    else stack.push(path[i])
  }

  return "/" + stack.join("/")
}

// simplifyPath("/../")
