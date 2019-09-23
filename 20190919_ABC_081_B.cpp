#include <bits/stdc++.h>
using namespace std;

int N;
int A[210];
int result = 0;

int main() {
  cin >> N;
  for (int i = 0; i < N; ++i) {
    cin >> A[i];
  }

  while (true) {
    bool exist_odd = false;

    for (int i = 0; i < N; ++i) {
      if (A[i] % 2 != 0) exist_odd = true;
    }

    if (exist_odd) break;

    for (int i = 0; i < N; ++i) {
      //   A[i] = A[i] / 2;
      A[i] /= 2;
    }
    ++result;
  }
  cout << result << endl;
}