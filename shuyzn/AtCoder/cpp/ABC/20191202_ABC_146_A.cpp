#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

int main() {
  string S;
  cin >> S;
  if (S == "SAT") cout << 1 << endl;
  if (S == "FRI") cout << 2 << endl;
  if (S == "THU") cout << 3 << endl;
  if (S == "WED") cout << 4 << endl;
  if (S == "TUE") cout << 5 << endl;
  if (S == "MON") cout << 6 << endl;
  if (S == "SUN") cout << 7 << endl;
  return 0;
}

// int main() {
//   string s[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
//   string t;
//   cin >> t;
//   rep(i, 7) {
//     if (s[i] == t) cout << 7 - i << endl;
//   }
//   return 0;
// }