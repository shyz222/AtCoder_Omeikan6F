#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

int top, s[1000];

int pop() {
  // return s[top];
  // top--; //returnで呼び出し元に戻っちゃうからだめ
  top--;
  return s[top + 1];
}

void push(int x) {
  top++;
  s[top] = x;
}

// O(1)
int main() {
  int a1, a2;
  top = 0;
  string c;
  while (cin >> c) {  // 標準入力が与え続けられるまで(EOFで終われる)
    if (c == "+") {
      a2 = pop();  // popは2番目のものからしてる
      a1 = pop();
      push(a1 + a2);
    } else if (c == "-") {
      a2 = pop();
      a1 = pop();
      push(a1 - a2);
    } else if (c == "*") {
      a2 = pop();
      a1 = pop();
      push(a1 * a2);
    } else {
      push(atoi(c.c_str()));
      // atoi()はchar*をintに変換
      // c_str()はstringをchar*に変換
      // char*はポインタ、char b[]は配列
    }
  }
  cout << pop() << endl;

  return 0;
}