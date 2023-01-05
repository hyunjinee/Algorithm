# 1491. Average Salary Excluding the Minimum and Maximum Salary

![1491](https://user-images.githubusercontent.com/63354527/106991485-ab91c580-67b9-11eb-90e5-31ca1c74a055.PNG)

문제해석: 정수로 된 배열이 주어진다. 그 값 하나는 고용자들의 월급이다.
가장 큰 값 가장 작은 값을 제외하고 고용자들의 평균 월급을 계산해라.

## 풀이1

가장 큰 요소를 찾아서 splice 메서드로 제거 그후에 평균을 구해서 반환했다.

```javascript
var average = function (salary) {
  salary.splice(salary.indexOf(Math.max(...salary)), 1);
  salary.splice(salary.indexOf(Math.min(...salary)), 1);

  let sum = 0;
  for (let all of salary) {
    sum += all;
  }
  return sum / salary.length;
};
```

마지막 부분 reduce 처리

```javascript
var average = function (salary) {
  // Remove Max. & Min.
  salary.splice(salary.indexOf(Math.max(...salary)), 1);
  salary.splice(salary.indexOf(Math.min(...salary)), 1);

  // Return Avg.
  return salary.reduce((acc, val) => acc + val) / salary.length;
};
```

## 풀이 2

```javascript
var average = function (salary) {
  salary.sort((a, b) => a - b);
  let arr = [];
  for (let i = 1; i < salary.length - 1; i++) {
    arr.push(salary[i]);
  }
  return arr.reduce((acc, cur) => acc + cur, 0) / arr.length;
};
```

## 풀이 3

```javascript
var average = function (salary) {
  const minSalary = Math.min.apply(null, salary);
  const maxSalary = Math.max.apply(null, salary);
  let totalSalary = salary.reduce((acc, curr) => acc + curr, 0);
  return (totalSalary - minSalary - maxSalary) / (salary.length - 2);
};
```
