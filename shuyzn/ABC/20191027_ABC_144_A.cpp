#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int A;
  cin >> A;
  int B;
  cin >> B;
  if (A > 9 || B > 9)
    cout << -1 << endl;
  else
    cout << A * B << endl;
}

// int main() {
//   int A;
//   cin >> A;
//   int B;
//   cin >> B;
//   if (A >= 1 && A <= 9 && B >= 1 && B <= 9)
//     cout << A * B << endl;
//   else
//     cout << -1 << endl;
// }