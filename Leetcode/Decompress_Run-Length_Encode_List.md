# 1313. Decompress Run-Length Encoded List

문제 해석: 실행 길이 인코딩으로 압축 된 목록을 나타내는 정수 목록 번호가 제공됩니다.
인접한 각각의 원소들을 고려해라. 각각의 쌍은 freq원소 value val이 합쳐져있다.(sublist에) 모든 서브리스트를 합쳐라. 왼쪽에서 오른쪽으로 압축된것을 푼 리스트를 만들기위해서. 그리고, 리턴해라 푼 리스트를
내가 해야되는거는 쌍으로 주어진 숫자가있고 [1,2] 요런 식으로 있으면, 빈번도가 1이고 value는 2라는 거니까 2가 한번 나오는거다. [3,4] 는 빈번도가 3번 value가 4 즉 [4,4,4]

풀이1

```javascript
var decompressRLElist = function (nums) {
  let lst = [];
  for (let i = 0; i < nums.length; i = i + 2) {
    for (let j = 0; j < nums[i]; j++) {
      lst.push(nums[i + 1]);
    }
  }
  return lst;
};
```

풀이2

```javascript
var decompressRLElist = function (nums) {
  let length = nums.length;
  let result = [];
  for (let i = 0; i < length; i += 2) {
    result.push(...new Array(nums[i]).fill(nums[i + 1]));
  }
  return result;
};
```
