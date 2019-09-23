// #include <bits/stdc++.h>
// using namespace std;

// int a, b;

// int main() {
//   cin >> a >> b;
//   if (a * b % 2 == 0) {
//     cout << 'Even' << endl; //「'」は１文字を表すためだけに利用なので誤り
//   } else {
//     cout << '&Odd' << endl; //「'」は１文字を表すためだけに利用なので誤り
//   }
// }

#include <bits/stdc++.h>
using namespace std;

int a, b;

int main() {
  cin >> a >> b;
  if (a * b % 2 == 0) {
    cout << "Even" << endl;
  } else {
    cout << "Odd" << endl;
  }
}