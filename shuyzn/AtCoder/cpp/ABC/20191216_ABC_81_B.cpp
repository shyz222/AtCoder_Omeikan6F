#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  int a[210];
  cin >> n;
  rep(i, n) cin >> a[i];
  int cnt = 0;
  bool flag = true;
  while (flag) {
    rep(i, n) {
      if (a[i] % 2 != 0) {
        flag = false;
        break;
      }
      a[i] /= 2;
      if (i == n - 1) cnt++;
    }
  }
  cout << cnt << endl;
  return 0;
}