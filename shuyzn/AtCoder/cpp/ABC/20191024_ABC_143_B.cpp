#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  int d[110];
  rep(i, N) cin >> d[i];

  int res = 0;
  rep(i, N) {
    // d[i]とd[i+1]~d[N-1]を各々掛けて合算。d[i]d[i+1]+d[i]d[i+2]+・・・+d[i]d[N-1]
    for (int j = i + 1; j < N; j++) {
      int ptrn = d[i] * d[j];
      res += ptrn;
    }
  }
  cout << res << endl;
}