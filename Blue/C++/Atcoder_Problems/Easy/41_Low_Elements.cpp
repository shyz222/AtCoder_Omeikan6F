#include <bits/stdc++.h>
#define endl '\n'
#define INF 2e9
#define int ll
typedef long long ll;
using namespace std;

signed main()
{
  cin.tie(0);
  cout.tie(0);
  ios::sync_with_stdio(false);
  int N;
  cin >> N;
  int min_i = N + 1;
  int ans = 0;
  for (int i = 0; i < N; i++)
  {
    int P;
    cin >> P;
    min_i = min(min_i, P);
    if (min_i == P)
    {
      ans++;
    }
  }
  cout << ans << endl;
}