# 1448. Count Good Nodes in Binary Tree

[문제 보러가기](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## 🅰 설계

재귀로 순회해서 전의 값중 가장 큰값보다 크면 ++ 해주자.

## ✅ 후기

> js

```js
var goodNodes = function (root) {
  let res = 0;
  const dfs = (node, preMax) => {
    if (!node) return;
    if (node.val >= preMax) res++;
    dfs(node.left, Math.max(node.val, preMax));
    dfs(node.right, Math.max(node.val, preMax));
  };
  dfs(root, -Infinity);
  return res;
};
```

> python

```py
class Solution:
    def goodNodes(self, root: TreeNode, mx=float('-inf')) -> int:
        # base case
        if not root: return 0

        # compare current value with current max in path
        if root.val >= mx:
            # add 1 (good node) + sum of good nodes in left and right
            # also change new max to this node
            return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(
                root.right, root.val)
        else:
            # this is bad node, but keep looking for good nodes
            return self.goodNodes(root.left, mx) + self.goodNodes(
                root.right, mx)
```

```py
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=[1]
        maxm=root.val
        def recursion(node,count,maxm):
            if not node:
                return
            if not node.left and not node.right:
                return
            if node.left:
                if node.left.val>=maxm:
                    count[0]=count[0]+1
                    recursion(node.left,count,node.left.val)
                else:
                    recursion(node.left,count,maxm)
            if node.right:
                if node.right.val>=maxm:
                    count[0]=count[0]+1
                    recursion(node.right,count,node.right.val)
                else:
                    recursion(node.right,count,maxm)
        recursion(root,count,maxm)
        return count[0]

```

> java

```java
class Solution {
    int good;
    public int goodNodes(TreeNode root) {
        good = 0;
        cal(root, Integer.MIN_VALUE);
        return good;
    }
    void cal(TreeNode root, int max){
        if(root == null) return;
        if(root.val >= max) good++;
        max = Math.max(max, root.val);
        cal(root.left, max);
        cal(root.right, max);
    }
}
```

// 새롭게 알게되거나 공유해서 알게된 점

트리를 공부하고 있었다. 좀더 트리에대한 이해가 깊어져야할 것같다. 특히 재귀를 쓰는 부분.

// 고생한 점
