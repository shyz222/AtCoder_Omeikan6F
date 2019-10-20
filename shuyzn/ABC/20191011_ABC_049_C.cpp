#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
  string S;
  cin >> S;

  string wrd[4] = {"dream", "dreamer", "erase", "eraser"};
  //文字列を後ろから判定したいため文字を左右反転する
  reverse(S.begin(), S.end());                      // Sを左右反転
  rep(i, 4) reverse(wrd[i].begin(), wrd[i].end());  // wrdの各々を左右反転

  bool matchAllWrd =
      true;  //全ての文字列がwrd[]の組み合わせでマッチするかフラグ

  //↓のforはrep使っちゃダメ！！ループ後処理がi++じゃないから
  // rep(i,S.size())はアウト
  for (int i = 0; i < S.size();) {
    bool matchPartWrd =
        false;  //文字列の一部がwrd[]のいずれかとマッチするかフラグ
    rep(k, 4) {
      string w = wrd[k];
      if (S.substr(i, w.size()) == w) {
        matchPartWrd = true;
        ////↓これが今回のループ後処理になっている
        ///※部分文字列パターンマッチ時のみ
        i += w.size();
      }
    }
    if (!matchPartWrd) {
      matchAllWrd = false;
      break;
    }
  }

  if (matchAllWrd)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
}
