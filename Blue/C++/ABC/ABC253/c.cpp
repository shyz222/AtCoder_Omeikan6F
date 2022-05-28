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
using namespace std;
//配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    multiset<ll> s;
    int Q;
    cin>>Q;
    while(Q--){
        int t;
        cin >> t;
        if (t==1) {
            int x;
            cin >> x;
            s.insert(x);
        }
        else if (t==2) {
            int x, c;
            cin >> x >> c;
            while (c-- and s.find(x) != s.end()){
                // この評価式でmin(c, s.count(x)と同値になる
                // 値がmultisetに含まれない場合はend()を返すため
                s.erase(s.find(x));
            }
        }
        else {
            cout << *s.rbegin() - *s.begin() << endl;
        }
    }
}