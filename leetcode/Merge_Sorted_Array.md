# 88. Merge Sorted Array

![thinkplease](https://user-images.githubusercontent.com/63354527/108821661-48998e80-7601-11eb-9499-fbf2c385d225.PNG)

## 풀이1

```javascript
var merge = function (nums1, m, nums2, n) {
  var insertPos = m + n - 1;
  m--;
  n--;
  while (n >= 0) {
    nums1[insertPos--] = nums1[m] > nums2[n] ? nums1[m--] : nums2[n--];
    console.log(nums1);
  }
};
```

## 풀이 2

```javascript
var merge = function (nums1, m, nums2, n) {
  nums1.splice(m, nums1.length - m);

  var i = 0;
  var j = 0;

  while (j < nums2.length) {
    if (nums1[i] === undefined || nums1[i] > nums2[j]) {
      nums1.splice(i, 0, nums2[j]);
      j++;
      i++;
    } else {
      i++;
    }
  }
};
```
