# 1694. Reformat Phone Number

![1694](https://user-images.githubusercontent.com/63354527/108310318-80b26300-71f6-11eb-917e-fc97bee54acf.PNG)

## 풀이 1

정규표현식으로 맞는거를 찾아서 배열을 받고 그걸 조인시켜서 문자열을 만든다. 그리고 3개씩짜르고, -를 붙인다. 나머지는 시키는대로 했다.

```javascript
var reformatNumber = function (number) {
  let re = /[0-9]/g;
  let ans = number.match(re).join("");
  let temp = [];
  let i = 0;
  while (ans.length - i > 4) {
    temp.push(...ans.slice(i, i + 3));
    temp.push("-");
    i += 3;
  }

  let leftover = ans.slice(i);
  if (leftover.length == 4) {
    temp.push(leftover.slice(0, 2));
    temp.push("-");
    temp.push(leftover.slice(2));
  } else {
    temp.push(leftover);
  }
  return temp.join("");
};
```

## 풀이 2

```javascript
var reformatNumber = function (number) {
  let numArr = number.replace(/-/g, "").replace(/ /g, "").split("");
  let res = "";
  while (numArr.length >= 4) {
    numArr.length == 4
      ? (res +=
          numArr.splice(0, 2).join("") + "-" + numArr.splice(0, 2).join(""))
      : (res += numArr.splice(0, 3).join("") + "-");
  }
  res += numArr.join("");
  return res;
};
```

## 풀이 3

```javascript
var reformatNumber = function (number) {
  number = number.split("-").join("").split(" ").join("");
  let res = "";

  for (let i = 0; i < number.length; i += 3) {
    if (number.slice(i, number.length).length > 4) {
      res += number.slice(i, i + 3);
      res += i + 3 !== number.length ? "-" : "";
    } else {
      const remainingNumbers = number.slice(i, number.length).length;
      switch (remainingNumbers) {
        case 4:
          res += number.slice(i, i + 2) + "-" + number.slice(i + 2, i + 4);
          return res;
        default:
          res += number.slice(i, i + remainingNumbers);
          return res;
      }
    }
  }
  return res;
};
```
