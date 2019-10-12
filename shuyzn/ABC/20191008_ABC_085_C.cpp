#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  using ll = long long;
  ll Y;
  cin >> Y;
  int res10000 = -1, res5000 = -1, res1000 = -1;
  // N=a+b+cを意識する
  rep(a, N + 1) {
    rep(b, N - a + 1) {
      int c = N - a - b;
      int total = 10000 * a + 5000 * b + 1000 * c;
      if (total == Y) {
        res10000 = a;
        res5000 = b;
        res1000 = c;
      }
    }
  }
  cout << res10000 << " " << res5000 << " " << res1000 << endl;
}