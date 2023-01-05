# 557. Reverse Words in a String III

![reversing](https://user-images.githubusercontent.com/63354527/107746183-bf5c9f00-6d58-11eb-896b-0593a2f09f83.PNG)

## 풀이 1

```javascript
var reverseWords = function (s) {
  let ans = [];
  let temp = s.split(" ");
  temp.forEach((e) => ans.push([...e].reverse().join("")));

  return ans.join(" ");
};
```

```javascript
var reverseWords = function (s) {
  return s
    .split(" ")
    .map((w) => w.split("").reverse().join(""))
    .join(" ");
};
```

## 풀이 2 stack

```javascript
var reverseWords = function (s) {
  let res = "";
  let word = "";
  for (let c of s) {
    if (c === " ") {
      res += word + c;
      word = "";
    } else {
      word = c + word;
    }
  }
  return res + word;
};
```
