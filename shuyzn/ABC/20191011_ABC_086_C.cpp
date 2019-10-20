#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  int t[110000], x[110000], y[110000];
  cin >> N;
  // 初期状態
  t[0] = x[0] = y[0] = 0;
  // t[1]x[1]y[1]からt[N]x[N]y[N]までの入力
  rep(i, N) cin >> t[i + 1] >> x[i + 1] >> y[i + 1];

  bool canTravel = true;
  rep(i, N) {
    int dt = t[i + 1] - t[i];
    int dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i]);
    if (dt < dist) canTravel = false;
    if (dist % 2 != dt % 2) canTravel = false;
  }

  if (canTravel)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
}
