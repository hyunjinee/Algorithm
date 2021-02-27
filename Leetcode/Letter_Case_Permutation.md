# Letter Case Permutation

![letter](https://user-images.githubusercontent.com/63354527/108700111-7ae7b500-7549-11eb-99ab-8152a70463ab.PNG)

## 풀이 1

솔직히 너무 개판이었다. 답과 맞추기 위해 일단 별시도를 다해서 맞춘답이긴하다. 다른 사람의 코드를 보자!

```javascript
var letterCasePermutation = function (S) {
  let isAllnumber = 0;
  for (let k = 0; k < S.length; k++) {
    if (S[k].match(/[0-9]/)) isAllnumber++;
  }
  if (isAllnumber == S.length) {
    return [S];
  }
  S = S.toLowerCase();
  S = S.split("");
  let ans = [];
  let i = 0;
  for (i = 0; i < S.length; i++) {
    if (S[i].match(/[a-z]/)) {
      break;
    }
  }
  ans.push(S.slice(0, i + 1).join(""));
  ans.push(ans[0].toUpperCase());

  for (i = i + 1; i < S.length; i++) {
    if (S[i].match(/[a-z]/)) {
      console.log(ans.length, "?");
      let length = ans.length;
      for (let j = 0; j < length; j++) {
        ans.push(ans[j] + S[i]);
        ans.push(ans[j] + S[i].toUpperCase());
        console.log(j);
      }
    } else {
      ans = ans.map((_) => {
        return _ + S[i];
      });
    }
  }
  ans = ans.filter((e) => e.length === S.length);
  return ans;
};
```

## 풀이 2

재귀호출.. 개멋있따

```javascript
var letterCasePermutation = function (S) {
  let permutaion = [];
  letterCasePermutationIndex(S, 0, permutaion, "");
  return permutaion;
};

var letterCasePermutationIndex = function (S, i, arr, prefix) {
  if (i < S.length) {
    let c = S.charAt(i).toLowerCase();
    letterCasePermutationIndex(S, i + 1, arr, prefix + c);
    if (c >= "a") {
      letterCasePermutationIndex(S, i + 1, arr, prefix + c.toUpperCase());
    }
  } else {
    arr.push(prefix);
  }
};
```

## 풀이 3

진짜 개멋이ㄸㅆ다..ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
이렇게 잘해지자 나도..

```javascript
var letterCasePermutation = function (S) {
  S = S.toLowerCase();
  let len = S.length,
    ans = [];
  const dfs = (i, res = "") => {
    if (i < len) {
      dfs(i + 1, res + S[i]);
      if (S[i] >= "a") dfs(i + 1, res + S[i].toUpperCase());
    } else ans.push(res);
  };
  dfs(0);
  return ans;
};
```
