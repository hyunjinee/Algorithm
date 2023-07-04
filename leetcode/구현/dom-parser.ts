export const html = (str: TemplateStringsArray, ...args: unknown[]) => {
  console.log(str, args)

  const resultHTML = str.map((s, i) => `${s}${args[i] || ""}`).join("")
  console.log(resultHTML)

  const parser = new DOMParser()

  const doc = parser.parseFromString(resultHTML, "text/html")
  console.log(doc)
  return doc.body
}

html`
  <div>
    <div>${"hello world"}</div>
    <div>${"hello world"}</div>
  </div>
`
