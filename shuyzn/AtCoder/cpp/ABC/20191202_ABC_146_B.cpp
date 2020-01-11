#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;

int main() {
  int n;
  string s;
  cin >> n;
  cin >> s;
  // cのアドレスをnだけ加算
  // ZのときはAに変換
  // 範囲for文for(変数宣言:範囲)、pythonでもみた気がする
  // &cはcのアドレス値
  // 範囲for文の時は変数宣言が実態(c)だとダメ、アドレス値の加減算できない
  for (char &c : s) {
    rep(i, n) {
      if (c == 'Z')
        c = 'A';
      else
        c++;  // 次の文字にする
    }
  }

  // // ↑と同様の処理
  // for (int i = 0; i < s.end() - s.begin(); i++) {
  //   rep(j, n) {
  //     if (s[i] == 'Z')
  //       s[i] = 'A';
  //     else
  //       s[i]++; // 次の文字にする
  //   }
  // }

  cout << s << endl;
  return 0;

  // // 次の文字になる
  // char c;
  // cin >> c;
  // cout << ++c << endl;
  // // 3番目の文字が次の文字になる
  // string s;
  // cin >> s;
  // s[2]++;
  // cout << s << endl;
}
