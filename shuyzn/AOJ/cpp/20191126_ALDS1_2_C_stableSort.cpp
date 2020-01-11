#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

// データ構造を定義する機能。classと似てる
//（Cardクラス作ったよ的な感じ。Cardストラクト作ったよ的な）
struct Card {
  char suit;
  int num;
};  //セミコロン忘れずに

//配列出力処理
void output(struct Card a[], int n) {
  rep(i, n) {
    if (i > 0) {
      cout << " ";
    }
    cout << a[i].suit << a[i].num;
  }
  cout << endl;
}

// bubble Sort
// 安定ソート
void bubbleSort(struct Card a[], int n) {
  // int cnt = 0;
  bool flag = true;
  while (flag) {
    flag = false;
    for (int i = n - 1; i > 0; i--) {
      if (a[i].num < a[i - 1].num) {
        swap(a[i], a[i - 1]);
        // cnt++;
        flag = true;
      }
    }
  }
  output(a, n);
  // cout << cnt << endl;
}

// selection Sort
// 安定ソートではない
void selectionSort(struct Card a[], int n) {
  // int cnt = 0;
  rep(i, n) {
    int minIndex = i;
    for (int j = i; j < n; j++) {
      if (a[j].num < a[minIndex].num) {
        minIndex = j;
      }
    }
    swap(a[i], a[minIndex]);
    // if (i != minIndex) cnt++;  // 交換回数の条件はiとminIndexが異なる場合
  }
  output(a, n);
  // cout << cnt << endl;
}

//安定判定
bool isStable(struct Card a[], struct Card b[], int n) {
  rep(i, n) {
    if (a[i].suit != b[i].suit) return false;
    // return来たら、その場でその時の戻り値もって呼び出し元へいく
  }
  return true;
}

// O(n^2)
int main() {
  int n;
  Card a[40], b[40];
  cin >> n;
  rep(i, n) cin >> a[i].suit >> a[i].num;
  // rep(i, n) cin >> b[i].suit >> b[i].num;
  rep(i, n) b[i] = a[i];  //↑と同等処理
  bubbleSort(a, n);
  cout << "Stable" << endl;  // バブルソートは安定だから
  selectionSort(b, n);
  if (isStable(a, b, n)) {
    cout << "Stable" << endl;
  } else {
    cout << "Not stable" << endl;
  }
  return 0;
}
