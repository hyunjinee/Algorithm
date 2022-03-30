# 1402. Reducing Dishes

[문제 보러가기](https://leetcode.com/problems/reducing-dishes/)

## 🅰 설계

정렬한다음 모든 원소에대해 계산하면 될것같아요 ㅎ\_ㅎ

## ✅ 후기

> javascript

```js
var maxSatisfaction = function (satisfaction) {
  satisfaction.sort((a, b) => a - b);

  let max = 0;

  for (let i = 0; i < satisfaction.length; i++) {
    let tempMax = 0;
    for (let j = i, k = 1; j < satisfaction.length; j++, k++) {
      tempMax += satisfaction[j] * k;
    }
    max = Math.max(max, tempMax);
  }

  return max;
};
```

// 새롭게 알게되거나 공유해서 알게된 점

브루트포쓰..

// 고생한 점

X
