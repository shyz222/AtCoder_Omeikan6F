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
    int A,B,M;
    cin>>A>>B>>M;
    vi a(A);
    vi b(B);
    vector<vector<int>> sale(M,vi (3));
    REP(i,0,A){
        cin >> a[i];
    }
    REP(i,0,B){
        cin >> b[i];
    }
    REP(i,0,M){
    cin>>sale[i][0]>>sale[i][1]>>sale[i][2];
    }
    int ans =  *min_element(all(a)) + *min_element(all(b));
    REP(i,0,M){
        int tmp = a[sale[i][0]-1] + b[sale[i][1]-1] - sale[i][2];\
        ans = min(ans,tmp);
    }
    cout<<ans<<endl;
}