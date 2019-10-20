#include <bits/stdc++.h>
using namespace std;

int fact(int n) {  //階乗関数
  if (n == 0) return 1;
  return n * fact(n - 1);
}

int main() {
  int n;                    //入力用の箱
  cin >> n;                 //標準入力
  cout << fact(n) << endl;  //階乗関数使って出力
}