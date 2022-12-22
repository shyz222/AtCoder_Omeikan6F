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
  int a, b;
  cin >> a >> b;
  if (0 < a)
  {
    cout << "Positive" << endl;
  }
  else if (a < 0 && b < 0)
  {
    if ((b - a + 1) % 2 == 0)
    {
      cout << "Positive" << endl;
    }
    else
    {
      cout << "Negative" << endl;
    }
  }
  else
  {
    cout << "Zero" << endl;
  }
  return 0;
}