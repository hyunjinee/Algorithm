// insertnode 
// ('값', 왼쪽, 오른쪽)


#include <stdio.h>
#include <stdlib.h>

typedef struct treeNode 
{
    int elem;
    treeNode* left;
    treeNode* right;
} treeNode;

treeNode* insertNode(int elem, treeNode* left, treeNode* right)
{
    treeNode* v = (treeNode*) malloc(sizeof(treeNode) * 1);
    v -> elem;
    v -> left;
    v -> right;
    return v;
}

int isInternal(treeNode *v) 
{
    return (( v-> left != NULL) && v -> right != NULL );
}

treeNode * leftChild(treeNode *v) 
{
    return v-> left;
}

treeNode* rightChild(treeNode *v)
{
    return v -> right;
}

treeNode* treeBuild()
{
    treeNode* n1 = insertNode('H', NULL, NULL);
    treeNode* n2 = insertNode('I', NULL, NULL);
    treeNode* n3 = insertNode('E', n1, n2);
    treeNode* n4 = insertNode('D', NULL, NULL);
    treeNode* n5 = insertNode('B', n4, n3);
    treeNode* n6 = insertNode('F', NULL, NULL);
    treeNode* n7 = insertNode('G', NULL, NULL);
    treeNode* n8 = insertNode('C', n6, n7);
    treeNode* n9 = insertNode('H', n5, n8);

}

void visit(treeNode* v) 
{
    printf("%d", v -> elem);
}

void binaryPreOrder(treeNode *v) 
{
    visit(v);
    if (isInternal(v))
    {
        binaryPreOrder(leftChild(v));
        binaryPreOrder(rightChild(v));

    }
}


int main() 
{
    treeNode* root = treeBuild();
    binaryPreOrder(root);

    return 1;


}
