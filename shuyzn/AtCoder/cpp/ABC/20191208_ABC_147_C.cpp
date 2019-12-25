#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  cin >> n;
  int g[15][15];  // 証言の2次元配列0が嘘つき1が正直-1が証言なし
  rep(i, n) rep(j, n) g[i][j] = -1;  // 初期値証言なし
  rep(i, n) {
    int a;
    cin >> a;
    rep(j, a) {
      int x, y;
      cin >> x >> y;
      --x;  // 0起点で合わせるため
      g[i][x] = y;
    }
  }
  int res = 0;
  //「正直者(1)」「不親切な人(0)」の2^Nパターンの部分集合を列挙して全探索
  rep(i, 1 << n) {
    vector<int> d(n);
    rep(j, n) if (i >> j & 1) d[j] =
        1;  // iで1がたっている場所の動的配列に1を入れる
    bool ok = true;
    rep(j, n) {
      // d[j]=1つまり正直者がいた場合、証言も正直者といっているか確認する
      if (d[j]) {
        rep(k, n) {
          if (g[j][k] == -1) continue;  // 証言がない場合は飛ばす
          if (g[j][k] != d[k])
            ok = false;  //証言があり、一致しない場合okをfalseに
        }
      }
    }
    if (ok)
      res = max(res, __builtin_popcount(i));  // iを2進数で表示したときの1の数
  }
  cout << res << endl;
  return 0;
}

// #include <bits/stdc++.h>
// using namespace std;

// int N;
// int A[20];
// int x[20][20];
// int y[20][20];

// int counter(int x) {
//     if(x == 0) return 0;
//     return counter(x >> 1) + (x & 1);
// }

// void solve() {
//     cin >> N;
//     for(int i = 1; i <= N; i++) {
//         cin >> A[i];
//         for(int j = 1; j <= A[i]; j++) {
//             cin >> x[i][j] >> y[i][j];
//         }
//     }
//     int ans = 0;
//     for(int bits = 1; bits < (1 << N); bits++) {
//         bool ok = true;
//         for(int i = 1; i <= N; i++) {
//             if(!(bits & (1 << (i-1)))) continue;
//             for(int j = 1; j <= A[i]; j++) {
//                 if(((bits >> (x[i][j]-1)) & 1) ^ y[i][j]) ok = false;
//             }
//         }
//         if(ok) ans = max(ans, counter(bits));
//     }
//     cout << ans << endl;
//     return;
// }

// int main() {
//     solve();
//     return 0;
// }
