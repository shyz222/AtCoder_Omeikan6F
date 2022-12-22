#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define rrep(i,a,b) for(int i=a;i>=b;i--)
#define endl '\n'
#define INF 2e9
#define int ll
typedef long long ll;
using namespace std;

signed main() {
  int N, M;
  vector<vector<int>> A(31, vector<int>(31));
  cin >> N >> M;
  vector<int> like(M, 0);
  rep(i, 0, N) {
    int k; cin >> k;
    rep(j, 0, k) {
      int a; cin >> a;
      like[a-1]++;
    }
  }
  int ans = 0;
  rep(i, 0, M) {
    if (like[i]==N) {
      ans++;
    }
  }
  cout << ans << endl;
}
