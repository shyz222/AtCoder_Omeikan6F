#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int a, b;
  cin >> a >> b;
  if (a == 1) {
    if (b == 2) cout << 3 << endl;
    if (b == 3) cout << 2 << endl;
  }
  if (a == 2) {
    if (b == 1) cout << 3 << endl;
    if (b == 3) cout << 1 << endl;
  }
  if (a == 3) {
    if (b == 1) cout << 2 << endl;
    if (b == 2) cout << 1 << endl;
  }
  return 0;
}