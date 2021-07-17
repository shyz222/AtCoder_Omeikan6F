#include <bits/stdc++.h>
#define REP(i, a, n) for (int i = a; i < n; i++)
#define REPR(i, n) for(int i = n; i >= 0; i--)
#define FOR(i, m, n) for(int i = m; i < n; i++)
#define endl    '\n'
#define INF 2e9
#define int ll
#define vi          vector<int>
#define de          deque<int>
#define SZ(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()//全範囲指定を簡略化
typedef long long ll;
using namespace std;
//配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int N,K;
    map<int, int> mp;
    cin>>N>>K;
    vi c(N);
    REP(i,0,N) cin >> c[i];

    REP(i,0,K) mp[c[i]]++;
    int ans = mp.size();
    REP(i,K,N){
        mp[c[i]]++;
        mp[c[i-K]]--;
        if(mp[c[i-K]] == 0) mp.erase(c[i-K]);
        ans = max(ans, (int)mp.size());
    }
    cout << ans << endl;
}