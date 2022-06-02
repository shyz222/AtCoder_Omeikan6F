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

//回転行列を使って求める
//θ=90°なので、回転行列は、((0,1)(1,0))となり、回転後は(-y, x)となる
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int x_1, y_1, x_2, y_2;
    cin>>x_1>>y_1>>x_2>>y_2;
    int dx = x_2 - x_1;
    int dy = y_2 - y_1;
    int x = x_2, y = y_2;
    REP(i, 0, 2) {
        int _dx = -dy;
        int _dy = dx;
        dx = _dx;
        dy = _dy;
        x += dx;
        y += dy;
        cout << x << " " << y;
        if (i==0)
            cout << " ";
        else
            cout << endl;
    }
}