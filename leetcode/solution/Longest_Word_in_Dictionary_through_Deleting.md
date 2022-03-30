# Longest Word in Dictionary through Deleting

![position](https://user-images.githubusercontent.com/63354527/108738562-16434f00-7577-11eb-91c8-c9ca82b4e842.PNG)

## 풀이 1

```javascript
var findLongestWord = function (S, D) {
  let ans = "";
  for (let word of D) {
    let a = word.length,
      b = ans.length;
    if (a < b || (a === b && word > ans)) continue;
    let pos = -1;
    for (let char of word) {
      console.log(S.indexOf(char, pos + 1));
      pos = S.indexOf(char, pos + 1);

      if (pos === -1) break;
    }
    if (pos !== -1) ans = word;
  }
  return ans;
};
```
