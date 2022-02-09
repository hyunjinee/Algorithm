#include <stdio.h>
#include <stdlib.h>
// 머리와 꼬리를 모두 가진다.
// 양방향 연결리스트의 각 노드는 앞 노드와 뒤 노드의 정보를 모두 저장합니다.
// 우리는 데이터를 '오름차순'으로 저장하는 양방향 연결리스트를 구현해 봅니다.!

typedef struct Node {
  int data;
  struct Node *next;
  struct Node *prev;
} Node;

Node *head, *tail;


void insert (int data) {
  Node* node = (Node*)malloc(sizeof(Node));
  node -> data = data;
  Node* cur;

  cur = head -> next;
  while (cur->data < data && cur != tail) {
    cur = cur -> next;
  }
  Node* prev = cur -> prev;
  prev -> next = node;
  node -> prev = prev;
  cur -> prev = node;
  node -> next = cur;
}

void removeFront () {
  Node* node = head->next;
  head->next = node -> next;
  
  Node* next = node -> next;
  next-> prev = head;
  free(node);
}

void show() {
  Node* cur = head -> next;
  while (cur != tail) {
    printf("%d ", cur ->data);
    cur = cur->next;
  }
}

int main(void) {
  head = (Node*) malloc(sizeof(Node));
  tail = (Node*) malloc(sizeof(Node));
  head -> next = tail;
  head -> prev = head;
  tail -> next = tail;
  tail -> prev = head;
  insert(2);
  insert(1);
  insert(3);
  insert(9);
  insert(7);
  removeFront();
  show();
  return 0;
}