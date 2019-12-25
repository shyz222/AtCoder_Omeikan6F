#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

int main() {
  int n, d, a, res;
  cin >> n >> d;
  a = n / (d * 2 + 1);
  if (n % (d * 2 + 1) > 0)
    cout << a + 1 << endl;
  else
    cout << a << endl;
  return 0;
}
