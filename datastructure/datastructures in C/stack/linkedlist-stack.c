#include <stdio.h>
#include <stdlib.h>

#define INF 9999999;

typedef struct {
  int data;
  struct Node* next;
} Node;


typedef struct {
  Node* top;
} Stack;

void push (Stack* stack, int data) {
  Node* node = (Node*) malloc(sizeof(Node));
  node -> data = data;
  node -> next = stack -> top;
  stack -> top = node;
}

int pop (Stack *stack) {
  if (stack -> top == NULL) {
    printf("스택 언더플로우가 발생했습니다.\n");
    return -INF;
  }
  Node* node = stack -> top;
  int data = node -> data;
  stack -> top = node -> next;
  free(node);
  return data;
}

void show (Stack* stack) {
  Node* cur = stack -> top;
  printf("--- 스택의 최상단 --- \n");
  while (cur != NULL) {
    printf("%d \n", cur -> data);
    cur = cur -> next;
  } 
  printf("--- 스택의 최하단 --- \n");
}

int main(void) {
  Stack stack;
  stack.top = NULL;
  show(&stack);
  push (&stack, 7);
  puch (&stack, 5);
  show (&stack);
  return 0;
}