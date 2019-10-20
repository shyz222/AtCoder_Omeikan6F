#include <bits/stdc++.h>
using namespace std;

int N;
int A[210];
bool oddFlag = false;
int res = 0;

int main() {
  cin >> N;                                 // Nの標準入力
  for (int i = 0; i < N; ++i) cin >> A[i];  // Aあるだけ標準入力

  while (true) {  //無限ループのこと。ほかにもwhile(1)やfor(;;)と書けるらしい
    for (int i = 0; i < N; ++i) {  // A[i]に奇数あるか確認
      if (A[i] % 2 == 1) oddFlag = true;
    }
    if (oddFlag == true) break;  // 奇数あったら終わり
    for (int i = 0; i < N; ++i) A[i] /= 2;
    ++res;
  }
  cout << res << endl;
}