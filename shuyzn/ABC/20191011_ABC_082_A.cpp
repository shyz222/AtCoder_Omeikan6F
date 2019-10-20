#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int a, b;
  cin >> a >> b;
  int mean = (a + b) / 2;
  if ((a + b) % 2 != 0)
    cout << mean + 1 << endl;
  else
    cout << mean << endl;
}
