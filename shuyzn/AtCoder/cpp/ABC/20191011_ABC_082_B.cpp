#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string s, t;
  cin >> s >> t;
  //↓文字列ソートの仕方
  sort(s.begin(), s.end());
  //↓greater<string>はない？→リファレンス確認
  //	sort(t.begin(),t.end(),greater<string>();
  sort(t.begin(), t.end());
  reverse(t.begin(), t.end());
  if (s < t)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
}
