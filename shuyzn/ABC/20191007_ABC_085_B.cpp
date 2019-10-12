#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

//バケット法
int main() {
  int N;
  cin >> N;
  int d[110];
  rep(i, N) cin >> d[i];
  int num[110] = {0};
  rep(i, N) num[d[i]]++;

  int res = 0;
  rep(i, 110) {
    if (num[i]) res++;
  }
  cout << res << endl;
}

// //連想配列
// int main() {
//   int N;
//   cin >> N;
//   int d[110];
//   rep(i, N) cin >> d[i];

//   set<int> values;  // insert するときに重複を取り除いてくれます
//   rep(i, N) values.insert(d[i]);  // 挿入します

//   // set のサイズを出力します
//   cout << values.size() << endl;
// }