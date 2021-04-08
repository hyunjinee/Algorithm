# 1464. Maximum Product of Two Elements in an Array

[문제 보러가기](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

## 🅰 설계

배열을 순회하고 가장 큰 값을 찾으면 가장 큰 값을 빼준다.다시순회해서 다음 큰 값을 찾는다.

## ✅ 후기

> javascript

```js
var maxProduct = function (nums) {
  console.log(Math.max(...nums));

  let temp = nums.splice(nums.indexOf(Math.max(...nums)), 1)[0];
  let temp1 = nums.splice(nums.indexOf(Math.max(...nums)), 1)[0];
  return (temp - 1) * (temp1 - 1);
};
```

> python

```python
class Solution(object):
    def maxProduct(self, nums):

        first, second = 0, 0

        for number in nums:

            if number > first:
                # update first largest and second largest
                first, second = number, first

            else:
                # update second largest
                second = max( number, second)

        return (first - 1) * (second - 1)
```

> java

```java
class Solution {
    public int maxProduct(int[] nums) {
        int max1 = 0;
        int max2 = 0;
        for(int i:nums){
            if(i>max1){
                max2 = max1;
                max1 = i;
            }
            else if(i>max2){
                max2 = i;
            }
        }
        return (max1-1)*(max2-1);
    }
}
```

// 새롭게 알게되거나 공유해서 알게된 점

없음.
// 고생한 점

없음.
