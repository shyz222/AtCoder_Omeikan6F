#include <bits/stdc++.h>
using namespace std;

int A, B, C, X;
int res = 0;
int sum = 0;

int main() {
  cin >> A >> B >> C >> X;
  for (int a = 0; a < A + 1; a++) {
    for (int b = 0; b < B + 1; b++) {
      for (int c = 0; c < C + 1; c++) {
        sum = 500 * a + 100 * b + 50 * c;
        if (sum == X) ++res;
      }
    }
  }
  cout << res << endl;
}