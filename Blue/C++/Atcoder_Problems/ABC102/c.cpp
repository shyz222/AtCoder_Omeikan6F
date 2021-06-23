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
    vi A(N),B(N);
    REP(i,N){
        cin >> A[i], B[i] = A[i] - i;
    };

    //メディアン
    sort(B.begin(), B.end());
    int x = B[N/2];

    //答え
    int ans = 0;
    REP(i,N){
        ans += max(x - B[i], -x + B[i]); // \A\ = max(A, -A)
    }
    cout << ans << endl;
}