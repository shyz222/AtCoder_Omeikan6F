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
  vs menu(5);
  int max_diff = 0, sum = 0, tmp_diff, diff_sum = 0;
  string tmp_menu;
  for (int i = 0; i < 5; i++)
  {
    cin >> tmp_menu;
    sum += stoi(tmp_menu);
    int tmp_str = int(tmp_menu.at(tmp_menu.size() - 1) - '0');
    if (tmp_str != 0)
    {
      tmp_diff = 10 - tmp_str;
      diff_sum += tmp_diff;
      max_diff = max(max_diff, tmp_diff);
    }
  }
  cout << sum + diff_sum - max_diff << endl;
}