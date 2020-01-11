#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int a, b;
  string s;
  cin >> a >> b;
  cin >> s;
  string res = "Yes";
  rep(i, s.size()) {
    if (i == a) {
      if (s[i] != '-') res = "No";
    } else if (!isdigit(s[i])) {
      res = "No";
    }
  }
  cout << res << endl;
  return 0;
}