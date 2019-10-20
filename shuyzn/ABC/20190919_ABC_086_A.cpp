#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  // cin >> a;
  // cin >> b;
  if (a * b % 2 == 0) {
    cout << "Even\n";
  } else {
    cout << "Odd\n";
  }
}