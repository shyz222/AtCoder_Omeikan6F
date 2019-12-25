#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

ll solve(string s) {
  ll cnt = 0, ret = 0;
  rep(i, s.size()) {
    cnt++;
    if (s[i] != s[i + 1] || i == s.size() - 1) {
      ret += cnt / 2;
      cnt = 0;
    }
  }
  return ret;
}

int main() {
  string s;
  ll k;
  ll res = 0;
  cin >> s;
  cin >> k;
  bool allSameChar = true;

  rep(i, s.size() - 1) {
    if (s[i] != s[i + 1]) allSameChar = false;
  }

  if (allSameChar) {
    res = (ll)s.size() * k / 2LL;
    cout << res << endl;
  } else {
    string ss = s + s;
    ll t = solve(s);
    ll tt = solve(ss);
    res = t + (tt - t) * (k - 1LL);
    cout << res << endl;
  }
  return 0;
}
