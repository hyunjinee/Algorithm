# 1436. Destination City

문제 해석: 너는 배열 paths가 주어질 것이다. paths[i] = [cityA, cityB]는 A에서B가는 직접적인 경로가 있다는 것을 의미한다. 다른 도시로 나가는 경로가 없는 목적지 city를 반환해라
그니까 연쇄적 배열을 주면 마지막 경로가 어딘지 찾으라는 문제이다.

## 풀이 1

일단 처음에 떠오른 것은 마지막에 대응하는 도시는 배열의 첫 값에 올수 없다는 것이다. 따라서 아래의 코드를 작성할 수 있었다.

```javascript
var destCity = function (paths) {
  for (let i = 0; i < paths.length; i++) {
    let count = 0;
    for (let j = 0; j < paths.length; j++) {
      if (paths[i][1] != paths[j][0]) {
        count++;
        if (count == paths.length) {
          break;
        }
      }
    }
    if (count == paths.length) {
      return paths[i][1];
      break;
    }
  }
};
```

## 풀이 2

다른 사람의 풀이를 읽어보니 Map객체로 쉽고빠르게 해결 한 것을 볼 수 있었다.

```javascript
var destCity = function (paths) {
  const p = new Map(paths);
  let des = paths[0][1];
  while (p.get(des)) {
    des = p.get(des);
  }
  return des;
};
```
