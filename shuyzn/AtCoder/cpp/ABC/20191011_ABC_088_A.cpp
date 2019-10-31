#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  int A;
  cin >> A;

  int kozeni = N % 500;
  if (kozeni <= A)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
}
