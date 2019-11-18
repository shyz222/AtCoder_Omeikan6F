#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

int main() {
  int n;
  int R[200000];
  cin >> n;
  rep(i, n) cin >> R[i];
  int maxm = R[1] - R[0];
  int minm = R[0];
  for (int i = 1; i < n; i++) {
    maxm = max(maxm, R[i] - minm);
    minm = min(minm, R[i]);  // iを増やしてく過程でR[i]の最小値を保持する
  }
  cout << maxm << endl;
  return 0;
}