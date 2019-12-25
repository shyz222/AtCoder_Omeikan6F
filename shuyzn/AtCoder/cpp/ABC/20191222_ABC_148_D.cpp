#include <bits/stdc++.h>

#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  int a[200010];
  cin >> n;
  rep(i, n) cin >> a[i];
  int cnt = 0;
  int num = 1;
  rep(i, n) {
    if (a[i] == num)
      num++;
    else
      cnt++;
  }
  if (cnt == n)
    cout << -1 << endl;
  else
    cout << cnt << endl;
  return 0;
}