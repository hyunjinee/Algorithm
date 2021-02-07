# 1507. Reformat Date

![1507](https://user-images.githubusercontent.com/63354527/106993382-ee559c80-67bd-11eb-9df1-57987dd47fbe.PNG)

문제해석: date문자열이 주어진다. (day month year 순)

포맷해라 그 문자열을. (YYYY-MM-DD)

## 풀이 1

그냥 안되는 것들을 다 걸러버렸다...ㅋㅋ

```javascript
var reformatDate = function (date) {
  const Month = {
    Jan: "1",
    Feb: "2",
    Mar: "3",
    Apr: "4",
    May: "5",
    Jun: "6",
    Jul: "7",
    Aug: "8",
    Sep: "9",
    Oct: "10",
    Nov: "11",
    Dec: "12",
  };

  date = date.split(" ");
  console.log(date);
  let ans = "";
  ans += date[2] + "-";
  if (Month[date[1]].length > 1) ans += Month[date[1]] + "-";
  else {
    ans += "0" + Month[date[1]] + "-";
  }

  let temp = "";
  for (let i = 0; i < date[0].length; i++) {
    if (
      date[0][i] != "t" &&
      date[0][i] != "h" &&
      date[0][i] != "n" &&
      date[0][i] != "d" &&
      date[0][i] != "r" &&
      date[0][i] != "s"
    )
      temp += date[0][i];
  }
  if (temp.length > 1) ans += temp;
  else {
    ans += "0" + temp;
  }

  return ans;
};
```

## 풀이 2

템플릿 문자열, 비구조화 할당

```javascript
// time O(1) space O(1)
var reformatDate = function (date) {
  const dateArray = date.split(" ");
  const [day, month, year] = dateArray;

  return `${year}-${formatMonth(month)}-${formatDay(day)}`;
};

function formatDay(day) {
  const isOneDigit = day.length === 3;

  if (isOneDigit) {
    return "0" + day[0];
  }

  return day[0] + day[1];
}

function formatMonth(month) {
  const months = {
    Jan: "01",
    Feb: "02",
    Mar: "03",
    Apr: "04",
    May: "05",
    Jun: "06",
    Jul: "07",
    Aug: "08",
    Sep: "09",
    Oct: "10",
    Nov: "11",
    Dec: "12",
  };

  return months[month];
}
```
