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
    int L,Q;
    cin>>L>>Q;
    tuple<int, int> query;
    vector<tuple<int, int>> query_list;
    REP(i,0,Q){
        cin >> c >> x;
        query_list.push_back(make_tuple(c, x));
    }
    vi remain_L(L-1,0);
    REP(i,0,Q){
        if(get<0>query_list[i]==1){
            remain_L[get<1>query_list[i]] = 1;
        }
        if(get<0>query_list[i]==1){
            if(remain_L[get<1>query_list[i]]==0){

            }
        }
    }
}