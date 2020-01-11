#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

// 20191206_ABC_146_C
int main() {
  ll a, b, x;
  cin >> a >> b >> x;
  ll f = 0, l = 1e9 + 1;
  // ラムダ式
  // &をつけるとラムダ式の外のスコープの変数も使えるようになる
  auto keta = [&](ll c) {
    // whileの条件について、0はfalse、0以外はtrue扱い
    int res = 0;
    while (c) {  // 桁数を求める
      c /= 10;
      res++;
    }
    return res;
  };

  // ラムダ式
  auto func = [&](ll c) { return a * c + b * keta(c); };

  // 2分探索
  while (l - f > 1) {
    ll c = (f + l) / 2;
    // cout << c << endl;
    if (func(c) <= x)
      f = c;
    else
      l = c;
  }
  cout << f << endl;
  return 0;
}
