#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  string s;
  cin >> s;
  string t = s;
  reverse(t.begin(), t.end());
  int cnt = 0;
  rep(i, s.length()) {
    if (s[i] != t[i]) cnt++;
  }
  cout << cnt / 2 << endl;
  return 0;
}