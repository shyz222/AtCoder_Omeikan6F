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
  // N=x+y+z
  rep(x, N + 1) {
    rep(y, N - x + 1) {
      int z = N - x - y;
      int total = 10000 * x + 5000 * y + 1000 * z;
      if (total == Y) {
        res10000 = x;
        res5000 = y;
        res1000 = z;
      }
    }
  }
  cout << res10000 << " " << res5000 << " " << res1000 << endl;
}
