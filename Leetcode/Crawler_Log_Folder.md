# 1598. Crawler Log Folder

![1598](https://user-images.githubusercontent.com/63354527/108441298-2964cf00-7298-11eb-8b6d-4a00f5373a5a.PNG)

# 풀이 1

```javascript
var minOperations = function (logs) {
  let agg = 0;
  for (let i = 0; i < logs.length; i++) {
    if (logs[i][0].match(/[0-9a-z]/)) agg++;
    else if (logs[i][0] == "." && logs[i][1] == ".") agg--;
    else continue;
    if (agg < 0) agg = 0;
    console.log(agg);
  }
  return agg < 0 ? 0 : agg;
};
```

## 풀이 2

```javascript
var minOperations = function (logs) {
  let depth = 0;

  for (const step of logs) {
    if (step === "./") {
      continue;
    } else if (step === "../") {
      depth--;
    } else {
      depth++;
    }

    if (depth < 0) {
      depth = 0;
    }
  }

  return depth;
};
```

## 풀이 3

```javascript
const minOperations = (logs) =>
  Math.abs(
    logs.reduce(
      (acc, curr) =>
        Math.min(0, acc + ("../" === curr ? 1 : "./" === curr ? 0 : -1)),
      0
    )
  );
```
