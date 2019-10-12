#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  int d[110];
  rep(i, N) cin >> d[i];

  int bkt[110] = {0};
  rep(i, N) bkt[d[i]]++;

  int res = 0;
  rep(i, 110) {
    if (bkt[i] >> 0) res++;
  }
  cout << res << endl;
}