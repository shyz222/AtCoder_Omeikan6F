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
  int s[15][15];
  rep(i, n) rep(j, n) s[i][j] = -1;  // -1は証言なしとする
  rep(i, n) {
    int a;
    cin >> a;
    rep(j, a) {
      int x, y;
      cin >> x >> y;
      --x;  //全て0起点で配列に格納するため
      s[i][x] = y;  // iさんはxさんのことをy(0:不親切,1:正直)と証言してる
    }
  }
  int res = 0;

  rep(i, 1 << n) {
    // 証言と一致してるか確認するために動的配列を用意する
    vector<int> t(n);
    rep(j, n) if (i >> j & 1) t[j] =
        1;  // iの2進数bitを動的配列に格納（証言配列sと連動させるため）
    bool ok = true;
    rep(j, n) {  // t[j]とs[j][]に対応させたループ
      if (t[j]) {
        // d[j]=1つまり正直者がいた場合、その正直者の証言が全て正しいか確認する
        rep(k, n) {
          //正直者の証言は全て正しいといけないため差異があればfalseに
          if (s[j][k] == -1) continue;
          if (s[j][k] != t[k]) ok = false;
        }
      }
    }
    if (ok) res = max(res, bitCounter(i));
  }
  cout << res << endl;
  return 0;
}
