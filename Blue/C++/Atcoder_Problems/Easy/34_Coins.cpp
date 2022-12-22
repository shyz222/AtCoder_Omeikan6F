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
// 配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める
signed main()
{
  cin.tie(0);
  cout.tie(0);
  ios::sync_with_stdio(false);
  int A, B, C, X;
  vector<int> n(4);
  REP(i, 0, 4)
  {
    cin >> n[i];
  }
  int ans = 0;

  for (int i = 0; i <= n[0]; i++)
  {
    for (int j = 0; j <= n[1]; j++)
    {
      for (int k = 0; k <= n[2]; k++)
      {
        int tmp_sum = i * 500 + j * 100 + k * 50;
        if (tmp_sum == n[3])
          ans++;
      }
    }
  }

  cout << ans << endl;
  return 0;
}