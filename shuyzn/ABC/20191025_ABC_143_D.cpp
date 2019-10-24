#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

// 条件がa<b+c,b<c+a,c<a+bと書いてあるが、
// ソートしたら、a<b<cのときa+b>cという条件になる←中学で習った気がする...

int main() {
  int n;
  cin >> n;
  int l[2000];
  rep(i, n) cin >> l[i];
  sort(l, l + n);
  int res = 0;
  rep(i, n) for (int j = i + 1; j < n; j++) {
    int ij = l[i] + l[j];
    int r = lower_bound(l, l + n, ij) - l;
    res += r - (j + 1);
  }
  cout << res << endl;
}

// vector使ってオッケーなやつ
// int main() {
//   int n;
//   cin >> n;
//   vector<int> L(n);
//   rep(i, n) cin >> L[i];
//   sort(L.begin(), L.end());
//   int ans = 0;
//   rep(a, n) for (int b = a + 1; b < n; b++) {  // rep(b, n) rep(a, b)も同義
//     int ab = L[a] + L[b];
//     int r = lower_bound(L.begin(), L.end(), ab) - L.begin();
//     int l = b + 1;
//     ans += r - l;
//   }
//   cout << ans << endl;
// }

// 実行時間長すぎでダメなやつ
// int main() {
//   int N;
//   cin >> N;
//   int L[10000];
//   rep(i, N) cin >> L[i];
//   int res = 0;
//   // a+b+c=Nとして探索
//   rep(a, N) {
//     for (int b = a + 1; b < N; b++) {
//       for (int c = b + 1; c < N; c++) {
//         if (L[a] < L[b] + L[c] && L[b] < L[c] + L[a] && L[c] < L[a] + L[b])
//           res++;
//       }
//     }
//   }
//   cout << res << endl;
// }

// 単純にロジックダメなやつ
// int main() {
//   int N;
//   cin >> N;
//   int L[10000];
//   rep(i, N) cin >> L[i];
//   int res = 0;
//   // a+b+c=Nとして探索
//   rep(a, N) {
//     for (int b = 0; b + a < N; b++) {
//       int c = N - a - b;
//       if (L[a] < L[b] + L[c] && L[b] < L[c] + L[a] && L[c] < L[a] + L[b])
//       res++;
//     }
//   }
//   cout << res << endl;
// }
