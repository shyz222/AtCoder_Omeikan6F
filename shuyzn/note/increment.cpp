#include <bits/stdc++.h>
using namespace std;

int n;

//インクリメント備忘録
int main() {
  cin >> n;
  // 1.後置インクリメント
  for (int i = 0; i < n; i++) {
    cout << i << endl;
    // cout << i << "\n";
  }
  // 2.前置インクリメント
  for (int i = 0; i < n; i++) {
    cout << i << endl;
    // cout << i << "\n";
  }
  // 1と2は結果同じ
  // ↓解説↓
  //「作用」→（副作用）
  // i++後置インクリメント：「iの値を返す」→(iにi+1を代入)
  // ++i前置インクリメント：「i+1の値を返す」→(iにi+1を代入)
  // for文では副作用の結果が使用されるので違いが出ない
  // 作用の結果が使用される場合は違いがでる
}