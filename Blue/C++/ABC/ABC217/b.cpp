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
    string S1, S2, S3;
    cin>>S1>>S2>>S3;
    vector<string> Contest = { "ABC", "AGC","ARC", "AHC"};
    auto itr = Contest.begin();
    while (itr != Contest.end())
    {
        if(((*itr) == S1) || ((*itr) == S2) || ((*itr)==S3))
        {
            itr = Contest.erase(itr);
        }
        else
        {
            itr++;
        }
    }
    cout<<Contest[0]<<endl;
}