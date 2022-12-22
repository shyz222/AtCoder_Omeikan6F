#include <bits/stdc++.h>
#define endl    '\n'
#define rep(i,a,b) for(int i=a;i<b;i++)
#define rrep(i,a,b) for(int i=a;i>=b;i--)
#define INF 2e9
#define int ll
typedef long long ll;
using namespace std;

signed main(){
  cin.tie(0);
  cout.tie(0);
  ios::sync_with_stdio(false);
  string w;
  vector<int> count(26);
  cin >> w;
  rep(i, 0, w.size()) count[(int)w[i] - 'a']++;
  rep(i, 0, 26) {
    if (count.at(i)%2 != 0) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}