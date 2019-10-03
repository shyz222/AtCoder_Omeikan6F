// #include <bits/stdc++.h>
// using namespace std;

// int N, A, B;
// int res;

// int main() {
//   cin >> N >> A >> B;
//   for (int i = 1; i <= N; i++) {
//     int sum;
//     while (true) {
//       sum += i % 10;
//       i /= 10;
//       if (i == 0) break;
//     }
//     if (A <= sum and B >= sum) res += sum;
//   }
//   cout << res << endl;
// }

#include <bits/stdc++.h>
using namespace std;

int N, A, B;
int res;

int findSumOfDigits(int n) {
  int sum = 0;
  while (n > 0) {
    sum += n % 10;
    n /= 10;
  }
  return sum;
}

int main() {
  cin >> N >> A >> B;
  for (int i = 1; i <= N; i++) {
    int sum = findSumOfDigits(i);
    if (sum >= A && sum <= B) res += i;
  }
  cout << res << endl;
}