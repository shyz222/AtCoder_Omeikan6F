// #include <bits/stdc++.h>
// using namespace std;

// string str;
// int res = 0;

// int main() {
//   cin >> str;
//   if (str[0] = '1') { //単純代入演算子「＝」になってる
//     ++res;
//   }
//   if (str[1] = '1') { //単純代入演算子「＝」になってる
//     ++res;
//   }
//   if (str[2] = '1') { //単純代入演算子「＝」になってる
//     ++res;
//   }
//   cout << res << endl;
// }

#include <bits/stdc++.h>
using namespace std;

string str;
int res = 0;

int main() {
  cin >> str;
  if (str[0] == '1') {
    ++res;
  }
  if (str[1] == '1') {
    ++res;
  }
  if (str[2] == '1') {
    ++res;
  }
  cout << res << endl;
}