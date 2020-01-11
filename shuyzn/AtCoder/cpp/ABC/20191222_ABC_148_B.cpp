#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  string s, t;
  cin >> n;
  cin >> s >> t;
  string res;
  rep(i, n) {
    res.append(1, s[i]);
    res.append(1, t[i]);
  }
  cout << res << endl;
  return 0;
}