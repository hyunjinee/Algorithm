# 500. Keyboard Row

![500](https://user-images.githubusercontent.com/63354527/107139525-1f210780-695f-11eb-8815-649bcd117ea6.PNG)

문제해석: 문자열로 이루어진 배열이 주어진다! 미국 키보드로, 한줄만 써서 칠수 있는 단어를 반환해라.

## 풀이 1

주어진대로 따라가보았다.

```javascript
var findWords = function (words) {
  let ans = [];
  let firstrow = "qwertyuiop".split("");
  let secondrow = "asdfghjkl".split("");
  let thirdrow = "zxcvbnm".split("");

  for (let word of words) {
    let count = 0;
    if (firstrow.indexOf(word[0].toLowerCase()) > -1) {
      for (let i = 0; i < word.length; i++) {
        if (firstrow.indexOf(word[i].toLowerCase()) > -1) {
          count++;
        }
      }
      if (count == word.length) ans.push(word);
    } else if (secondrow.indexOf(word[0].toLowerCase()) > -1) {
      for (let i = 0; i < word.length; i++) {
        if (secondrow.indexOf(word[i].toLowerCase()) > -1) {
          count++;
        }
      }
      if (count == word.length) ans.push(word);
    } else {
      for (let i = 0; i < word.length; i++) {
        if (thirdrow.indexOf(word[i].toLowerCase()) > -1) {
          count++;
        }
      }
      if (count == word.length) ans.push(word);
    }
  }
  return ans;
};
```

## 풀이 2

```javascript
var findWords = function (words) {
  const first_row = new Set("qwertyuiop");
  const second_row = new Set("asdfghjkl");
  const third_row = new Set("zxcvbnm");

  for (let i = 0; i < words.length; ++i) {
    let which = first_row;
    const first_character = words[i][0].toLowerCase();

    if (second_row.has(first_character)) which = second_row;
    else if (third_row.has(first_character)) which = third_row;

    for (let j = 0; j < words[i].length; ++j) {
      const letter = words[i][j].toLowerCase();

      if (!which.has(letter)) {
        words.splice(i, 1);
        --i;
        break;
      }
    }
  }

  return words;
};
```
