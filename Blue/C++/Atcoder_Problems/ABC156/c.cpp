#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; i < n; i++)
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
    int N;
    cin>>N;
    int ans = INF;
    vi vec(N);
    REP(i,N){
        cin >> vec[i];
    }
    int max_i = *max_element(vec.begin(),vec.end());
    int min_i = *min_element(vec.begin(),vec.end());
    for(int i=min_i;i<=max_i;i++){
        int tmp = 0;
        for(int j=0;j<N;j++){
            tmp += pow((vec[j]-i),2);
        }
        ans = min(ans, tmp);
    }
    cout<<ans<<endl;
}