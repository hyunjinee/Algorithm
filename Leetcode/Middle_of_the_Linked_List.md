# 876. Middle of the Linked List

![876](https://user-images.githubusercontent.com/63354527/107171499-4e3e8400-6a06-11eb-9dde-1b3f8ed0609e.PNG)

문제 해석: 비어있지않고, 단방향 연결된 링크드 리스트가 주어진다. 중간에 있는 노드를 반환해라 만약에, 2개면 두번째 것 반환해

```javascript
var middleNode = function (head) {
  let slow = head,
    fast = head;
  while (fast !== null) {
    fast = fast.next;
    if (fast == null) break;
    else fast = fast.next;

    slow = slow.next;
  }
  return slow;
  // Time Complexity: O(n)
  // Space Complexity: O(1)
};
```
