# 1021. Remove Outermost Parentheses

문제 해석: 타당한 괄호 문자열은 (""), "(" + A + ")", or A + B이다
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
위에 애들은 타당한 애들이다.
반환해라, 가장 바깥쪽 괄호를 지우고 S를 반환해라
일단 대충 해석하면 나눈다음에 바깥에 껍데기 빼고 더해서 결과를 리턴하라는 것 같다.

풀이1

```javascript
var removeOuterParentheses = function (S) {
  let count = 0;
  let startindex = 0;
  let ans = [];
  for (let i = 0; i < S.length; i++) {
    if (S[i] == "(") {
      count++;
    } else {
      count--;
    }
    if (count == 0) {
      let crust = S.slice(startindex, i + 1);
      startindex = i + 1;
      ans.push(crust);
    }
  }
  result = [];
  console.log(ans);
  ans.forEach((x) => {
    x = x.slice(1, -1);
    result.push(x);
  });
  return result.join("");
};
```

풀이2

```javascript
var removeOuterParentheses = function (S) {
  let res = []; //string buffer
  let tmpCnt = 0;
  let tmpStr = "";
  for (const c of S) {
    if (c === "(") {
      ++tmpCnt;
    } else if (c === ")") {
      --tmpCnt;
    }
    tmpStr += c;
    if (tmpCnt === 0) {
      res.push(tmpStr.substring(1, tmpStr.length - 1));
      tmpStr = "";
    }
  }
  return res.join("");
};
```
