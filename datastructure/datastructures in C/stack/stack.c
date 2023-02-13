#include <stdio.h>
#define INF 9999999
#define SIZE 1000

int stack[SIZE];
int top = -1;

void push(int data) {
  if (top == SIZE-1) {
    printf("스택 오버플로우가 발생했습니다.");
  }
  stack[++top] = data;
}

void pop () {
  if (top == -1) {
    printf("스택 언더플로우가 발생했습니다.\b");
    return -INF;
  }
  return stack[top--];
}

void show() {
  printf("--- 최상단 ---\n");
  for (int i = top; i>=0; i--) {
    printf("%d\n", stack[i]);
  }
  printf("--- 최하단 ---\n");
}

int main(void) {
  return 0;
}