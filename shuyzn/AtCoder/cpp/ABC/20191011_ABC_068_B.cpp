#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  int res = 1;
  while (res * 2 <= N) res *= 2;
  cout << res << endl;
}

// int main() {
//   int N;
//   cin >> N;
//   int res = 1;
//   do {
//     res *= 2;
//   } while (res <= N);
//   if (res > N) res /= 2;
//   cout << res << endl;
// }