#include <bits/stdc++.h>
#define REP(i, a, n) for (int i = a; i < n-1; i++)
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
    int K,N;
    cin>>K>>N;
    vi a(N);
    for(int i=0;i<N;i++){
        cin >> a[i];
    }
    int max_distance = 0;
    REP(i,0,N){
        max_distance = max(max_distance,a[i+1]-a[i]);
    }
    int end_start = K + a[0] - a[N-1];
    cout << min((K-max_distance),(K-end_start)) << endl;
}