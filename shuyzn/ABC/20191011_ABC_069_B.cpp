#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string s, res;
  cin >> s;
  int x = s.size();
  cout << s[0] << x - 2 << s[x - 1] << endl;
}

//↓これオッケー
// int main() {
//   string s;
//   cin >> s;
//   int N = s.length();
//   cout << s[0] << N - 2 << s[N - 1] << endl;
// }

//↓これダメ
// int main() {
//   string s, res;
//   cin >> s;
//   int x = s.size() - 2;
//   res = s[0] + (string)x + s[s.size()];
//   cout << res << endl;
// }
