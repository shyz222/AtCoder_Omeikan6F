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

// selection Sort
// 安定ソートではない
void selectionSort(int a[], int n) {
  int cnt = 0;
  rep(i, n) {
    int minIndex = i;
    for (int j = i; j < n; j++) {
      if (a[j] < a[minIndex]) {
        minIndex = j;
      }
    }
    swap(a[i], a[minIndex]);
    if (i != minIndex) cnt++;  // 交換回数の条件はiとminIndexが異なる場合
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
  selectionSort(a, n);
  return 0;
}
