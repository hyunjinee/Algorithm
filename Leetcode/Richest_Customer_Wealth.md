# 1672. Richest Customer Wealth

문제 해석: 너는 m, x, n 정수 그리드 어카운트들이 주어졌다. 근데 accounts[i][j]는 돈의 양이다. i번 째 고객이 j번째 은행에 있는돈.
wealth를 리턴해라 가장 돈 많은 고객의..
고객의 부는 계좌에 있는 돈이고 가장 부유한 고객은 가장 max wealth 이다.

풀이1

```javascript
var maximumWealth = function (accounts) {
  findmax = [];
  for (let i = 0; i < accounts.length; i++) {
    let sum = accounts[i].reduce((a, x) => a + x);
    findmax.push(sum);
  }
  //   console.log(typeof findmax[0]);
  return Math.max(...findmax);
};
```
