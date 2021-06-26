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
    int N;
    cin>>N;
    vector<double> l(N),r(N);
    REP(i,0,N){
        int t;
        cin>>t>>l[i]>>r[i];
        if(t==2){
            r[i]-= 0.5;
        }
        else if(t==3){
            l[i] += 0.5;
        }
        else if(t==4){
            l[i] += 0.5;
            r[i] -= 0.5;
        }
    }

    int count = 0;
    REP(i,0,N){
        REP(j,i+1,N){
            count += (max(l[i],l[j]) <= min(r[i],r[j]));
        }
    }
    cout << count << endl;
}