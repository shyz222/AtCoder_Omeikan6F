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
    int N,D,X;
    cin>>N;
    cin>>D>>X;
    vi a(N);
    REP(i,0,N){
        cin >> a[i];
    }
    int ate = 0;
    REP(i,0,N){
        REP(j,0,D){
            if(a[i]*j+1>D){
                break;
            }
            ate++;
        }
    }
    cout << X+ate << endl;
}