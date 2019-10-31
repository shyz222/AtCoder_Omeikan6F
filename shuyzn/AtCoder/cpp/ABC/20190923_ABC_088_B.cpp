#include <bits/stdc++.h>
using namespace std;

int N, a[110];
int alice = 0;
int bob = 0;

int main() {
  cin >> N;
  for (int i = 0; i < N; i++) cin >> a[i];
  sort(a, a + N, greater<int>());
  //   for (int i = 0; i < N; i++) {
  //     cout << a[i] << endl;
  //   }
  for (int i = 0; i < N; i++) {
    // 問題文ではalice奇数番目、bob偶数番目だが、
    // ループが0起点のためプログラム内では１つズレる
    if (i % 2 == 0) {
      alice += a[i];
    }
    if (i % 2 == 1) {
      bob += a[i];
    }
  }
  cout << alice - bob << endl;
}
