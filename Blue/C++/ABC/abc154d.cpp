#include <bits/stdc++.h>
#define INF 2e9
#define int ll
#define vi          vector<int>
#define vd          vector<double>
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
    int N, K;
    cin >> N >> K;
    
    vd p(N);
    vd s(N,0);
    for(int i=0;i<N;i++){
        cin >> p[i];
        s[i] = (p[i]+1)/2;
    }

    vd sum(N+1,0);
    for (int i = 0; i< N; i++){
        sum[i+1] = sum[i] + s[i];
    }

    double res = 0;
    for (int i=0; i <= N-K+1; i++){
        double val = sum[K+i] - sum[i];
        res = max(res,val);
    }
    
    cout << res << endl;
}