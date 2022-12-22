#include <bits/stdc++.h>
#define REP(i, a, n) for (int i = a; i < n; i++)
#define REPR(i, n) for (int i = n; i >= 0; i--)
#define FOR(i, m, n) for (int i = m; i < n; i++)
#define endl '\n'
#define INF 2e9
#define int ll
#define vi vector<int>
#define vs vector<string>
#define de deque<int>
#define SZ(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end() // 全範囲指定を簡略化
typedef long long ll;
typedef std::pair<int, int> pair;
#define vp vector<pair>
using namespace std;

// 累積和問題
signed main()
{
  cin.tie(0);
  cout.tie(0);
  ios::sync_with_stdio(false);
  int N, L_max = 0, R_max = 0;
  cin >> N;
  vi A(N), left(N + 1, 0), right(N + 1, 0);
  REP(i, 0, N)
  {
    cin >> A[i];
  }
  REP(i, 0, N)
  {
    left[i + 1] = max(left[i], A[i]);
    right[i + 1] = max(right[i], A[N - i - 1]);
  }
  REP(i, 0, N)
  {
    cout << max(left[i], right[N - i - 1]) << endl;
  }
}