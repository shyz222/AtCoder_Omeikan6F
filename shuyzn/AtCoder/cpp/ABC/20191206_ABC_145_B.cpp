#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  string s;
  cin >> n >> s;
  if (n % 2 == 1)
    cout << "No" << endl;
  else if (s.substr(0, n / 2) == s.substr(n / 2, n / 2))
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  // cout << s.substr(0, n / 2) << endl;
  // cout << s.substr(n / 2, n / 2) << endl;

  return 0;
}