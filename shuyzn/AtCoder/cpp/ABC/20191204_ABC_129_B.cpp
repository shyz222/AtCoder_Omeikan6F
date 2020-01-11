#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  int w[110], res = INT_MAX;
  cin >> n;
  rep(i, n) cin >> w[i];
  for (int j = 1; j < n; j++) {
    int s1 = 0, s2 = 0;
    for (int k = 0; k < j + 1; k++) s1 += w[k];
    for (int l = j + 1; l < n; l++) s2 += w[l];
    res = min(res, abs(s1 - s2));
  }
  cout << res << endl;
  return 0;
}
