#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  if (a + b + c >= 22)
    cout << "bust" << endl;
  else
    cout << "win" << endl;
  return 0;
}