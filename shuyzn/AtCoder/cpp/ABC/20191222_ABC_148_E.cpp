#include <bits/stdc++.h>

#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  ll n;
  cin >> n;
  ll cnt = 0;
  if (n % 2 == 1)
    cout << cnt << endl;
  else {
    n /= 2;
    while (n > 2) {
      n /= 5;
      cnt += n;
    }
    cout << cnt << endl;
  }

  return 0;
}