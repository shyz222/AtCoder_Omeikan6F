#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int bitCounter(int x) {
  if (x == 0) return 0;
  return bitCounter(x >> 1) + (x & 1);
}

// ビット全探索 +  α(証言と一致してるか確認する) アルゴリズム
int main() {
  int n;
  cin >> n;
  int g[15][15];
  rep(i, n) rep(j, n) g[i][j] = -1;
  rep(i, n) {
    int a;
    cin >> a;
    rep(j, a) {
      int x, y;
      cin >> x >> y;
      --x;
      g[i][x] = y;
    }
  }

  int res = 0;
  rep(i, 1 << n) {
    vector<int> h(n);
    // iは最大n回左ビットシフトなので、jからnでループさせてn個の動的配列にiのビットを格納する
    rep(j, n) if (i >> j & 1) h[j] = 1;
    bool ok = true;
    rep(j, n) {
      if (h[j]) {
        rep(k, n) {
          if (g[j][k] == -1) continue;
          if (g[j][k] != h[k]) ok = false;
        }
      }
    }
    if (ok) res = max(res, bitCounter(i));
  }
  cout << res << endl;
  return 0;
}
