#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  using ll = long long;
  ll A[N];
  rep(i, N) cin >> A[i];
  sort(A, A + N);
  int res = abs(A[N - 1] - A[0]);
  cout << res << endl;
}