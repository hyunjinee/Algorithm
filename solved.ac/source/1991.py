import sys


input = sys.stdin.readline


n = int(input())


tree ={}

def preorder(node):
    print(node, end="")
    left, right = tree[node][0] , tree[node][1]

    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

def inorder(node):
    left, right = tree[node][0], tree[node][1]
    if left != ".":
        inorder(left)
    
    print(node, end="")

    if right != '.':
        inorder(right)


def postorder(node):
    left, right = tree[node][0] , tree[node][1]

    if left != ".":
        postorder(left)

    if right != ".":
        postorder(right)
    
    print(node, end="")



for i in range(1, n+ 1):
    node, left, right = input().split()

    tree[node] = [left, right]

preorder('A'); print()
inorder('A'); print()
postorder('A'); print()