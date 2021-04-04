# 442번 Find All Duplicates in an Array

[문제 보러가기](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

## 🅰 설계

n개의 원소가 있고 O(n)을 원하므로 전체 순환이 한번된다.
배열을 직접순환하고 Set을 이용해서 만약 있다면 결과배열에 넣어서 마지막에 결과를 리턴해보자!!!

## ✅ 후기

> javascript

```js
var findDuplicates = function (nums) {
  let mySet = new Set();
  let ans = [];
  for (let i = 0; i < nums.length; i++) {
    if (mySet.has(nums[i])) ans.push(nums[i]);
    else {
      mySet.add(nums[i]);
    }
  }
  console.log(ans);
  return ans;
};
```

> python

```python
class Solution:
    def findDuplicates(self, N: List[int]) -> List[int]:
        S, A = set(), []
        for n in N:
            if n in S: A.append(n)
            else: S.add(n)
        return A

```

```py
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        rs = []
        for num in nums:
            num = abs(num)
            print(nums[num-1])
            if nums[num-1] < 0:
                print(nums[num-1])
                rs.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return rs
```

> java

```java
public class Solution {
    // when find a number i, flip the number at position i-1 to negative.
    // if the number at position i-1 is already negative, i is the number that occurs twice.

    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; ++i) {
            int index = Math.abs(nums[i])-1;
            if (nums[index] < 0)
                res.add(Math.abs(index+1));
            nums[index] = -nums[index];
        }
        return res;
    }
}
```

// 새롭게 알게되거나 공유해서 알게된 점
셋에 안넣고도 해결할 수 있었다. 문제조건에 따라서 n이하의 수로 만들어져 있으므로 그 인덱스를 음수로 바꾸고 만약 다시 그인덱스를 다시만났을 때 음수이면 바로 결과에 넣어 버린다.

// 고생한 점
다른사람의 풀이를 읽는데 인덱스에해당하는 수를 음수로 바꾸고 다시 그인덱스를 마주칠때 결과에 넣는 다는 것이 흥미로웠다.
