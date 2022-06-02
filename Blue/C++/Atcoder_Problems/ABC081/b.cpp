#include <bits/stdc++.h>
#define REP(i, a, n) for (int i = a; i < n; i++)
#define REPR(i, n) for(int i = n; i >= 0; i--)
#define FOR(i, m, n) for(int i = m; i < n; i++)
#define endl    '\n'
#define INF 2e9
#define int ll
#define vi          vector<int>
#define vs          vector<string>
#define de          deque<int>
#define SZ(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()//全範囲指定を簡略化
typedef long long ll;
typedef std::pair<int, int> pair;
#define vp          vector<pair>
using namespace std;
//配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int N;
    cin>>N;
    vi A(N);
    REP(i,0,N){
        cin >> A[i];
    }
    int ans = 0;
    bool flag = true;
    while (flag) {
        REP(i,0,N) {
            if(A[i]%2 == 0){
                A[i] = A[i]/2;
            }
            else{
                flag = false;
                break;
            }
        }
        if (!flag){break;}
        ans++;
    }
    cout<<ans<<endl;
}