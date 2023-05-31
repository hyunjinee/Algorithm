const numUniqueEmails = (emails) =>
  new Set(
    emails.map((a) => {
      const [local, domain] = a.split("@")
      return `${local.split("+")[0].split(".").join("")}@${domain}`
    })
  ).size
