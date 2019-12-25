#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

int main() {
  int n, a, b;
  cin >> n >> a >> b;
  if (n * a > b)
    cout << b << endl;
  else
    cout << n * a << endl;
  return 0;
}
