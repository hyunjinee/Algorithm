# 1370. Increasing Decreasing String

![1370](https://user-images.githubusercontent.com/63354527/106405795-b2979b80-647a-11eb-8afa-13e8aeb49a28.PNG)


문제 해석: 문자열 s가 주어진다. 너는, 이 문자열을 아래의 알고리즘을 이용하여서 재정렬하여야 한다.

1. s에서 가장 작은 문자를 선택하여 결과에 추가합니다.
2. 결과에 마지막으로 추가 된 문자보다 큰 s에서 가장 작은 문자를 선택하고 추가합니다.
3. 계속step 2를 반복해라. 더이상 뽑지 못할때 까지
4. 가장 큰 문자를 뽑고, 결과에 추가해라
5. 방금 뽑은것보다는 작지만 가장 큰 문자를 뽑아서 결과에 추가해라
6. 계속 반복해라 5번을 너가 더이상 못뽑을 때까지
7. 1~6을 계속 해라 니가 모든 문자를 뽑았을 때까지...

각각의 스텝에서, 만약 가장 작거나 가장 큰 문자가 한번이상 등장하면, 아무거나 추가해라
알고리즘 수행후의 s를 반환한다.

풀이1
일단 풀긴 했는데 너무 더럽게 풀어서 더고민 해봐야겠다.

```javascript
var sortString = function (s) {
  let length = s.length;
  recipe = [];
  s = s.split("");
  s.forEach((x) => {
    x = x.charCodeAt([0]);
    recipe.push(x);
  });
  result = [];
  let lastappended = 0;
  while (s.length > result.length) {
    let index = recipe.indexOf(Math.min(...recipe));
    let crust = recipe.splice(index, 1)[0];
    result.push(crust);
    lastappended = crust;
    let recipe3 = new Array(...recipe);

    recipe3.sort(function (a, b) {
      return a - b;
    });

    // while (true) {
    let smallest = [];
    for (let ele of recipe3) {
      if (ele > lastappended) {
        smallest.push(ele);
        recipe.splice(recipe.indexOf(ele), 1);
        lastappended = ele;
      }
    }
    console.log(smallest);

    result.push(...smallest);

    // }

    index = recipe.indexOf(Math.max(...recipe));
    crust = recipe.splice(index, 1)[0];
    result.push(crust);

    lastappended = crust;

    let largest = [];
    console.log(recipe);
    let recipe2 = new Array(...recipe);
    recipe2.sort(function (a, b) {
      return b - a;
    });

    for (let e of recipe2) {
      if (e < lastappended) {
        largest.push(e);
        recipe.splice(recipe.indexOf(e), 1);
        lastappended = e;
      }
    }

    result.push(...largest);
  }
  console.log(result[-1]);
  if (!result[-1]) {
    result[-1] = "";
  }
  result = result.filter((element, i) => element !== undefined);
  console.log(result[-1]);
  realresult = [];
  result.forEach((x) => {
    realresult.push(String.fromCharCode(x));
  });
  console.log(realresult[0]);
  console.log(realresult.join(""));
  console.log(realresult.join("").length);
  console.log(result[-1]);
  return realresult.join("");
};
```

풀이2

```javascript
var sortString = function (s) {
  const arr = s.split("").sort((x, y) => {
    if (x < y) return -1;
    if (x > y) return 1;
  });

  return getMaxOrMin(arr).join("");
};

function getMaxOrMin(arr) {
  if (!arr.length) return [];
  const ret = [];
  const deleteIndex = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== arr[i - 1]) {
      ret.push(arr[i]);
      deleteIndex.push(i);
    }
  }

  return [
    ...ret,
    ...getMaxOrMin(
      arr.filter((v, index) => deleteIndex.indexOf(index) === -1).reverse()
    ),
  ];
}
```

풀이3

```javascript
var sortString = function (s) {
  let arr = s.split("").sort();
  let set = Array.from(new Set(arr));
  let res = "";
  while (arr.length > 0) {
    for (let x of set) {
      res += x;
      arr.splice(arr.indexOf(x), 1);
    }
    set = Array.from(new Set(arr));
    for (let y of set.reverse()) {
      res += y;
      arr.splice(arr.indexOf(y), 1);
    }
    set = Array.from(new Set(arr));
  }
  return res;
};
```
