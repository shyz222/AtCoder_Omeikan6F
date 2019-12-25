#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

ll solve(string s) {
  ll cnt = 0, ret = 0;
  rep(i, s.size()) {
    cnt++;  // 基本カウントする
    // 文字が異なるとき、または最後の文字の時
    if (s[i] != s[i + 1] || i == s.size() - 1) {
      ret += cnt / 2;  // retに回数計上
      cnt = 0;         // cntリセット
    }
  }
  return ret;
}

int main() {
  string s;
  ll k;
  cin >> s;
  cin >> k;
  bool allSameChar = true;
  rep(i, s.size() - 1) {
    if (s[i] != s[i + 1]) allSameChar = false;
  }
  // 場合分け
  // 1全ての文字が同じ場合
  if (allSameChar) {
    cout << (ll)s.size() * k / 2LL << endl;
  } else {
    string ss = s + s;
    ll c = solve(s);
    ll cc = solve(ss);
    cout << c + (cc - c) * (k - 1LL) << endl;
  }
  return 0;
}
