#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string S;
  cin >> S;
  int count = 0;
  rep(i, 3) {
    if (S[i] == 'o') count++;
  }
  int res = 700 + 100 * count;
  cout << res << endl;
}
