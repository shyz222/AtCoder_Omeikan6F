#include <bits/stdc++.h>

#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

//ユークリッドの互除法
ll gcd(ll a, ll b) {  // greatest common divisor
  if (a < b) {
    a ^= b;  // xor使って入れ替えているだけ
    b ^= a;
    a ^= b;
  }
  //「式1 ? 式2 : 式 3」
  // 式1が真であれば式2を実行
  // 式1が偽であれば式3を実行
  // bが0以外なら真、0なら偽
  return b ? gcd(b, a % b) : a;
}

ll lcm(ll a, ll b) { return a * b / gcd(a, b); }  //

int main() {
  ll a, b;
  cin >> a >> b;
  ll res = lcm(a, b);
  cout << res << endl;
  return 0;
}