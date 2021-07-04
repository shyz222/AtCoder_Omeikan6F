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

template<class T>
auto comp_idx(T* ptr){
    return [ptr](int l_idx, int r_idx){
        return ptr[l_idx] < ptr[r_idx];
    };
}
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int N,K;
    cin>>N>>K;
    vi a(N);
    REP(i,0,N) cin >> a[i];

    int basic = K/N;
    int mod = K%N;
    vi ans(N);
    vi af_a(N);

    REP(i,0,N) ans[i] = basic;
    iota(af_a.begin(), af_a.end(), 0);
    sort(all(af_a),[&](int x,int y){return a[x]<a[y];});
    sort(all(a));
    REP(i,0,mod){
        ans[af_a[i]] += 1;
    }
    REP(i,0,N){
        cout << ans[i] << endl;
    }
}