#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int n;
  cin >> n;
  string ans = "No";
  for (int i = 1; i < 10; i++) {
    if (n / i >= 1 && n / i <= 9 && n % i == 0) {
      ans = "Yes";
    }
  }
  cout << ans << endl;
}