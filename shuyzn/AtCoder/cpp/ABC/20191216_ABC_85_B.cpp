#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  int d[110];
  cin >> n;
  rep(i, n) cin >> d[i];
  int num[110] = {0};  // 全ての配列要素が0と定義しないといけない
  rep(i, n) num[d[i]]++;
  int cnt = 0;
  rep(i, 110) if (num[i]) cnt++;
  cout << cnt << endl;
  return 0;
}