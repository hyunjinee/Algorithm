// 적정트리리란: 내부노드가 두개의 자식노드를 반드시 가져야한다.
// 외부노드: 자식 노드가 없는 노드를 말한다.
// 내부노드: 자식노드가 있는 노드를 말한다.


#include <stdio.h>
#include <stdlib.h> // 구ㅈ조체 동적할당

typedef struct treeNode
{
    int data;
    int id;
    treeNode* left;
    treeNode* right;
} treeNode;

treeNode* insertNode(int id, int data, treeNode* left, treeNode* right)
{
    treeNode* newNode = (treeNode*) malloc(sizeof(treeNode) * 1);
    newNode -> id = id;
    newNode -> data = data;
    newNode -> left = left;
    newNode -> right = right;
    return newNode;

}
treeNode* treeBuild()
{
    treeNode* n7 = insertNode(7,130,NULL,NULL);
    treeNode* n8 = insertNode(8,80,NULL,NULL);
    treeNode* n6 = insertNode(6,120,n7,n8);
    treeNode* n4 = insertNode(4,70,NULL,NULL);
    treeNode* n5 = insertNode(5,90,NULL,NULL);
    treeNode* n2 = insertNode(2,30,n4,n5);
    treeNode* n3 = insertNode(3,50,NULL,n6);
    treeNode* n1 = insertNode(1,20,n2,n3);

    return n1;

}

void visit(treeNode* v) {

}
// traverse
// preorder postorder inorder

void binaryPreOrder (treeNode * v)
{
    if (v!= NULL) 
    {
        visit(v);
        // binaryPreOrder();
        // binaryPreOrder(v);

    }
}

int main()
{
    return 0;
}