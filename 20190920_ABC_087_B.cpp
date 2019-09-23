// #include <bits/stdc++.h>
// using namespace std;

// int A, B, C, X;

// int main() {
//   cin >> A >> B >> C >> X;
//   for (int i; i < A + 1; ++i)
//   {//全部「i」じゃX=500*i+100*i+50*iになってしまうぞ
//     for (int i; i < B + 1; ++i) {
//       for (int i; i < C + 1; ++i) {
//       }
//     }
//   }
// }

// //↓全探索
// #include <bits/stdc++.h>
// using namespace std;

// int A, B, C, X;
// int sum;
// int res = 0;

// int main() {
//   cin >> A >> B >> C >> X;
//   for (int a; a < A + 1; ++a)
//   {//a,b,cの初期値決めていなかった。けどもコンパイル実行は問題なかった。結果がおかしかった
//     for (int b; b < B + 1; ++b) {
//       for (int c; c < C + 1; ++c) {
//         sum = 500 * a + 100 * b + 50 * c;
//         if (sum == X) ++res;
//       }
//     }
//   }
//   cout << res << endl;
// }

//↓全探索
#include <bits/stdc++.h>
using namespace std;

int A, B, C, X;
int sum;
int res = 0;

int main() {
  cin >> A >> B >> C >> X;
  for (int a = 0; a < A + 1; ++a) {
    for (int b = 0; b < B + 1; ++b) {
      for (int c = 0; c < C + 1; ++c) {
        sum = 500 * a + 100 * b + 50 * c;
        if (sum == X) ++res;
      }
    }
  }
  cout << res << endl;
}