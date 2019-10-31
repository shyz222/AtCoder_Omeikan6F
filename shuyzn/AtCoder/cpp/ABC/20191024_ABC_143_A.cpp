#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int A;
  cin >> A;
  int B;
  cin >> B;
  int res = A - 2 * B;
  if (res > 0)
    cout << res << endl;
  else
    cout << 0 << endl;
}