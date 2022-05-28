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

int ArithmeticSum(int a, int d, int n){
    return ((n * (2 * a + (n - 1) * d)) / 2);
}
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int n, a, b;
    cin >> n >> a >> b;
    int lc = a * b / __gcd(a, b);
    int n_a = n / a;
    int n_b = n / b;
    int n_l = n / lc;
    int sum_a = ArithmeticSum(a, a, n_a);
    int sum_b = ArithmeticSum(b, b, n_b);
    int sum_l = ArithmeticSum(lc, lc, n_l);
    int sum = ArithmeticSum(1, 1, n);
    cout << sum - sum_a - sum_b + sum_l << endl;
}