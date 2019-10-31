#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int N, a[110];
int alice = 0, bob = 0;

int main() {
  cin >> N;
  rep(i, N) cin >> a[i];
  sort(a, a + N, greater<int>());
  // greaterクラスは、左辺が右辺より大きいかの比較を行う関数オブジェクトである。
  //この関数オブジェクトは一切のメンバ変数を持たず、状態を保持しない。
  rep(i, N) {
    if (i % 2 == 0) alice += a[i];
    if (i % 2 == 1) bob += a[i];
  }
  cout << alice - bob << endl;
}