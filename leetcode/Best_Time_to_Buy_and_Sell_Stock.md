# Best Time to Buy and Sell Stock II

![sell](https://user-images.githubusercontent.com/63354527/109154511-b4baf480-77b1-11eb-8e38-e4fad705877f.PNG)

## 풀이

```javascript
var maxProfit = function (prices) {
  let profit = 0;

  for (let i = 1; i < prices.length; i++) {
    let prev = prices[i - 1];
    let current = prices[i];

    if (prev < current) {
      profit += current - prev;
    }
  }

  return profit;
};
```
