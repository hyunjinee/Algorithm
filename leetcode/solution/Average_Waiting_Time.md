# 1701.Average Waiting Time

![waitingtime](https://user-images.githubusercontent.com/63354527/109948414-a9ba1400-7d1d-11eb-8938-93fef21848d6.PNG)

## 풀이 1

고려할사항은 요리가 끝난시간이다. 요리가끝난시간보다 손님이 먼저 와있는가 와있지 않은가? 그리고 손님이 늦게오면 손님이 온시간에 맞추서 요리시작시간을 바꿔버린다.

```javascript
var averageWaitingTime = function (customers) {
  let waitingtime = [];
  let people = customers.length;
  let starttime = customers[0][0] + customers[0][1];
  waitingtime.push(customers[0][1]);
  for (let i = 1; i < customers.length; i++) {
    let cookingtime = customers[i][1];
    if (starttime < customers[i][0]) starttime = customers[i][0];
    starttime = starttime + cookingtime;
    if (starttime > customers[i][0])
      waitingtime.push(starttime - customers[i][0]);
    else waitingtime.push(customers[i][1]);
  }
  console.log(waitingtime);
  let sum = waitingtime.reduce((a, x) => a + x, 0);
  console.log(sum);
  return sum / people;
};
```

## 풀이 2

```javascript
var averageWaitingTime = function (C) {
  let time = 0,
    wait = 0;
  for (let [a, b] of C) (time = Math.max(time, a) + b), (wait += time - a);
  return wait / C.length;
};
```
