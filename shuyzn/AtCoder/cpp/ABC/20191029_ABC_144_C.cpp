#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;  // typedef long long ll でもいける

int main() {
  ll n;
  cin >> n;
  ll ans = 1e18;  // 10^18のこと
  // n<=1e12であるので、√nなら計算しきれる（√n=1e6だから）
  // min(a,b)<=√nの性質を利用して解く
  for (ll i = 1; i * i <= n; i++) {
    if (n % i == 0) {
      ll j = n / i;
      ans = min(ans, i + j - 2);
    }
    cout << ans << endl;
  }
}

// int main() {
//   ll n;
//   cin >> n;
//   int i, j;
//   ll sum = n + 1;
//   for (i = 1; i < n + 1; i++) {
//     if (n % i == 0) {
//       j = n / i;
//       if (sum > i + j) sum = i + j;
//     }
//   }
//   cout << sum - 2 << endl;
// }