#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int r, g, b;
  cin >> r >> g >> b;
  int total = 100 * r + 10 * g + 1 * b;
  if (total % 4 == 0)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
}
