#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int a, b, c, x;
  cin >> a >> b >> c >> x;
  int cnt = 0;
  rep(i, a + 1) {
    rep(j, b + 1) {
      rep(k, c + 1) {
        if (500 * i + 100 * j + 50 * k == x) cnt++;
      }
    }
  }
  cout << cnt << endl;
  return 0;
}