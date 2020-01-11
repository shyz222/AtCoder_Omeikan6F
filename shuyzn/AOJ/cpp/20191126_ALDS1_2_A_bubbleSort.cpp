#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

//配列出力処理
void output(int a[], int n) {
  rep(i, n) {
    if (i > 0) {
      // cout << " ";
      printf(" ");  //要素間に空白を入れる
    }
    // cout << a[i];
    printf("%d", a[i]);  //フォーマット指定子 %c char %d int10進数
  }
  // cout << endl;
  printf("\n");
}

// bubble Sort
// 安定ソート
void bubbleSort(int a[], int n) {
  int cnt = 0;
  bool flag = true;
  while (flag) {
    flag = false;
    for (int i = n - 1; i > 0; i--) {
      if (a[i] < a[i - 1]) {
        // int buf = a[i];
        // a[i] = a[i - 1];
        // a[i - 1] = buf;
        swap(a[i], a[i - 1]);  //↑3行と同様処理
        cnt++;
        flag = true;
      }
    }
  }
  output(a, n);
  cout << cnt << endl;
}

// O(n^2)
int main() {
  int n;
  int a[1000];
  cin >> n;
  rep(i, n) cin >> a[i];
  bubbleSort(a, n);
  return 0;
}
