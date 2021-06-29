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
    int A,B,C;
    cin>>A>>B>>C;
    int ans = 0;
    if((A==B)&&(B==C)&&((A%2==0))){
        cout << -1 << endl;
        return 0;
    }
    while(A%2==0&&B%2==0&&C%2==0){
        int tmp_A,tmp_B,tmp_C;
        tmp_A = (B+C)/2;
        tmp_B = (A+C)/2;
        tmp_C = (A+B)/2;
        A = tmp_A;B = tmp_B;C = tmp_C;
        ans++;
    }
    cout << ans << endl;
}