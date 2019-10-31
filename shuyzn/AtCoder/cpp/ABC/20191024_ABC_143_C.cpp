#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  string S;
  cin >> S;
  int res = 0;
  // 連続する文字が異なる箇所をカウントする
  rep(i, N) {
    if (S[i] != S[i + 1]) res++;
  }
  cout << res << endl;
}