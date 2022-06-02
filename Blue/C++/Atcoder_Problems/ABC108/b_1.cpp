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

struct Point {
    int x, y;
    Point(int _x, int _y) : x(_x), y(_y) {}
    Point() {}
    Point operator+(const Point &rhs) {
        return Point(this->x + rhs.x, this->y + rhs.y);
    }

    Point operator-(const Point &rhs) {
        return Point(this->x - rhs.x, this->y - rhs.y);
    }
};

inline Point Rotate90(const Point &p){
    return Point(-p.y, p.x);
}

signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    vector<Point> p(4);
    REP(i,0, 2){
        cin >> p[i].x >> p[i].y;
    };
    REP(i, 2, 4){
        p[i] = Rotate90(p[i - 1] - p[i - 2]) + p[i - 1];
    }
    for (int i = 2; i < 4; ++i){
        cout<< p[i].x << ' ' << p[i].y << (i == 3 ? '\n' : ' ');
    }
    return 0;
}